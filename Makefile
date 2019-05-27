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
# install path: /usr/bin
deb:
	@python setup.py --command-packages=stdeb.command bdist_deb

# install path: /usr/local/bin
deb-fpm:
	@fpm -s python -t deb ../handy/setup.py

rpm-fpm:
	@fpm -s python -t rpm ../handy/setup.py

install-deb:
	@dpkg --force-overwrite -i deb_dist/python-handi_$$(version handy)-1_all.deb

install-deb-fpm:
	@dpkg --force-overwrite -i python-handi_$$(version handy)_all.deb

clear:
	@cmds=$$(python -c "from config import commands; print(' '.join(commands))");\
	 for cmd in $$cmds; do rm -f $$(which $$cmd); done
	@rm -rf *.pyc

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

.PHONY: build install clear

