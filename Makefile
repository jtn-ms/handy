# detect operating system
ifeq ($(OS),Windows_NT)
    CURRENT_OS := Windows
else
    CURRENT_OS := $(shell uname -s)
endif

all: update install

# setup
build: clean
	pyinstaller --clean --distpath=dist handy.spec

install:
	pip install -U handi

setup:
	#pip install -e git+http://github.com/gustavkkk/handy.git#egg=handy
	python setup.py install

test:
	pytest

pypi: copy register upkg

github: login upsrc

# config
config: login copy register

login:
ifeq ($(CURRENT_OS),Windows)
	@echo "type mail:"
	@set /p mail=""
	@echo "type username:"
	@set /p username=""
	@echo "type password:"
	@set /p password=""
	@git config --global user.email "%mail%"
	@git config --global user.name "%username%"
	@git remote set-url origin https://%username%:%GITHUB_PASSWORD%@github.com/gustavkkk/handy.git
else
	@read -p "type mail:" mail;\
	read -p "type username:" username;\
	read -p "type password: " password;\
	git config --global user.email "$$mail"\
	git config --global user.name "$$password"\
	git remote set-url origin https://$$username:$$password@github.com/gustavkkk/handy.git	
endif


copy:
ifeq ($(CURRENT_OS),Windows)
	@copy .pypirc %USERPROFILE%
else
	@cp .pypirc $(HOME)
	@read -p "type username:" username;\
	read -p "type password: " password;\
	sed -i s/usrname/$$username/g $(HOME)/.pypirc;\
	sed -i s/passphrase/$$password/g $(HOME)/.pypirc
endif

register:
	@python3 setup.py register

# update
update: upsrc uppkg

upsrc: clean
ifeq ($(CURRENT_OS),Windows)
	@git add .
	@echo "type comment:"
	@set /p comment=""
	@git commit -m "%comment%"
	@git push origin master
else
	@git add .
	@read -p "type comment: " comment;\
	git commit -m "$$comment";\
	git push origin master
endif

upkg:
	@python3 setup.py sdist upload
	
# clean part
clean: 
ifeq ($(CURRENT_OS),Windows)
	@del /q /s *.bak
	@del /q /s *.pyc
	@del /q /s *.log
	@rmdir /q /s __pycache__
	@rmdir /q /s .pytest_cache
	@rmdir /q /s src
	@rmdir /q /s dist
	@rmdir /q /s build
	@rmdir /q /s handi.egg-info
else
	@find -name "*.pyc" -exec rm -f {} \;
	@find -name "*.log" -exec rm -f {} \;
	@find -name "*.deb" -exec rm -f {} \;
	@find -name "*.bak" -exec rm -f {} \;
	@find -name "*.tar.gz" -exec rm -f {} \;
	@find -name dist | xargs rm -rf
	@find -name .cache | xargs rm -rf
	@find -name build | xargs rm -rf
	@find -name handi.egg-info | xargs rm -rf
	@find -name .pytest_cache | xargs rm -rf
	@find -name __pycache__ | xargs rm -rf
	@find -name deb_dist | xargs rm -rf
	@find -name debian | xargs rm -rf
endif

# version:
# 	@cur_ver=$$(python -c "f=open('handy/handy.conf', 'r');\
# 										 versions=[line.strip().split('=')[1].strip(' \'\"') for line in f if line.startswith('__version__')];\
# 										 f.close();\
# 										 version= versions[0] if len(versions)>0 else '0.0.1';\
# 										 print(version)");\
# 	 echo current version: $$cur_ver;\
# 	 read -p "type new version: " new_ver;\
# 	 sed -i s/$$cur_ver/$$new_ver/g handy/_version.py

version:
	@git describe --tags `git rev-list --tags --max-count=1`

release: upsrc
	@cur_tag=$$(git describe --tags `git rev-list --tags --max-count=1`);\
	 echo current version: $$cur_tag;\
	 read -p "type new version: " new_tag;\
	 git tag $$new_tag;\
	 git push origin --tags

pre:
	@dpkg -P scala

# problem: version 0.0.1
#		   python module not installed	
# install path: /usr/bin
# deb:
# 	@python setup.py --command-packages=stdeb.command bdist_deb
# install-deb:
# 	@dpkg --force-overwrite -i deb_dist/python-handi_$$(version handy)-1_all.deb

# install path: /usr/local/bin
deb-pre:
	@apt-get install ruby ruby-dev rubygems build-essential
	@gem install --no-ri --no-rdoc fpm

deb:
	@fpm -s python -t deb ../handy/setup.py

rpm:
	@fpm -s python -t rpm ../handy/setup.py

install-deb:
	@dpkg --force-overwrite -i python-handi_$$(version handy)_all.deb

# apt
# http://www.linux-admins.net/2012/08/creating-apt-repository-with-reprepro.html
genkey: apt-conf
	@apt-get install gnupg dpkg-sig reprepro
	@gpg --gen-key

delkey:
	@gpg --delete-secret-keys GustavPi
	@gpg --delete-keys GustavPi

apt: clean on deb rmapt mkapt off

apt-conf: apt-conf-dir apt-conf-dist apt-conf-options apt-conf-override

apt-conf-dir:
	@if ! [ -d "/var/packages/ubuntu/conf" ]; then mkdir -p /var/packages/ubuntu/conf; fi
	@if ! [ -d "/var/packages/debian/conf" ]; then mkdir -p /var/packages/debian/conf; fi

apt-conf-dist:
	@if ! [ -f "/var/packages/ubuntu/conf/distributions" ]; then \
	 cp apt/distributions /var/packages/ubuntu/conf; fi

apt-conf-options:
	@if ! [ -f "/var/packages/ubuntu/conf/options" ]; then \
	 cp apt/options /var/packages/ubuntu/conf; fi

apt-conf-override:
	@if ! [ -f "/var/packages/ubuntu/conf/override.precise" ]; then touch /var/packages/ubuntu/conf/override.precise; fi

mkapt: apt-conf
	@debfile=$(CURDIR)/python-handi_$$(version handy)_all.deb;\
	 dpkg-sig --sign builder $$debfile;\
	 cd /var/packages/ubuntu;\
	 reprepro includedeb precise $$debfile

chkapt:
	@cd /var/packages/ubuntu;\
	 reprepro list precise

rmapt:
	@if [ -d "/var/packages/ubuntu" ]; then cd /var/packages/ubuntu;\
	 			  						   reprepro remove precise python-handi; fi

# local part
DOMAIN= packages.linux-admins
IPADDR = 192.168.10.124
KEYNAME = Anton Vos
addapt:
	@if [ "$$(findstr ${IPADDR} /etc/apt/sources.list)" == "" ]; then \
		echo "deb http://${IPADDR}/ubuntu precise main" >> /etc/apt/sources.list;\
		echo "deb-src http://${IPADDR}/ubuntu precise main" >> /etc/apt/sources.list;fi

start-apache2:
	@apt install apache2
	@cd /var/www/;\
	 cp $(CURDIR)/apt/repo.conf /etc/apache2/sites-available;\
	 gpg --armor --output html/${DOMAIN}.key --export "${KEYNAME}";\
	 a2ensite repo;\
	 service apache2 reload

stop-apache2:
	@cd /var/www/;\
	 a2dissite repo;\
	 systemctl stop apache2

apt-install:
	@curl -H GET ${IPADDR}/${DOMAIN}.key > $(CURDIR)/${DOMAIN}.key;
	@cp -rf /var/packages/ubuntu /var/www/html/ubuntu
	@apt-key add ${DOMAIN}.key
	@apt update
	@apt install python-handi
	@rm $(CURDIR)/${DOMAIN}.key

apt-remove:
	@deline "deb http://${IPADDR}" /etc/apt/sources.list
	@deline "deb-src http://${IPADDR}" /etc/apt/sources.list
	@apt remove python-handi
	
# https://www.maketecheasier.com/setup-local-repository-ubuntu/
# upapt2:
# 	@cd /var/www/;\
# 	 mkdir -p debs;\
# 	 cd debs;\
# 	 mkdir -p amd64 i386;\
# 	 debfile=$(CURDIR)/python-handi_$$(version $(CURDIR)/handy)_all.deb;\
# 	 cp $$debfile amd64;\
# 	 dpkg-scanpackages amd64 | gzip -9c > Packages.gz;
# 	@if [ "$$(findstr ${IPADDR} /etc/apt/sources.list)" == "" ]; then \
# 	  echo "deb http://${IPADDR}/debs/ amd64/" >> /etc/apt/sources.list;fi

# remove all installed exection files
# and print all
uninstall:
	@pip uninstall handi
	@cmds=$$(python -c "from config import commands; print(' '.join(commands))");\
	 for cmd in $$cmds; do rm -f $$(which $$cmd); done
	@rm -rf *.pyc

# ppa part
# https://askubuntu.com/questions/71510/how-do-i-create-a-ppa/493577#493577
# keyword: mmta
# https://launchpad.net/~falcon0125/+archive/ubuntu/pyhandy
# https://help.launchpad.net/Packaging/PPA/Uploading
# Note that Launchpad builds the packages onsite, and does not accept deb files. The correct command for creating the Debian package source is 'debuild -S'.
# python not supported by debuild -S
srcpkg: on
	@python setup.py sdist bdist_wheel

ppa-ftp:
	@apt install dput
	@cp apt/.dput.cf ~
	@dput ppa:falcon0125/pyhandy <source.changes> 

# misc
publish:
	@cmds=$$(python -c "from config import commands; print(' '.join(commands))");\
	 for cmd in $$cmds; do if [ "$$cmd" != "boo" ] && \
	 						  [ "$$cmd" != "cls" ] && \
							  [ "$$cmd" != "commit" ] && \
							  [ "$$cmd" != "bashrc" ] && \
							  [ "$$cmd" != "version" ] && \
							  [ "$$cmd" != "chkstdin" ] && \
							  [ "$$cmd" != "chkbashrc" ]; then $$cmd|row 2|fromstr "Usage: "; fi; done
	@rm -rf *.pyc

# Manual Versioning Flag
status:
	@findstr use_manual_versioning setup.py 
on:
	@replconfval setup.py use_manual_versioning False True
	@replconfval versioneer.py use_manual_versioning False True

off:
	@replconfval setup.py use_manual_versioning True False
	@replconfval versioneer.py use_manual_versioning True False

.PHONY: build install clear \
		upapt

