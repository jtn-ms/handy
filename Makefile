# detect operating system
ifeq ($(OS),Windows_NT)
    CURRENT_OS := Windows
else
    CURRENT_OS := $(shell uname -s)
endif

all: up upload install

install:
	pip install -U handi

setup:
	pip install -e git+http://github.com/gustavkkk/handy.git#egg=handy
	
# repo management part
login:
	git config --global user.email "gustav0125@outlook.com"
	git config --global user.name "gustavkkk"

up:
ifeq ($(CURRENT_OS),Windows)
	@git add .
	@echo "Enter a Comment:"
	@set /p comment=""
	@git commit -m %comment%
	@git push origin master
else
	@git add .
	@read -p "Enter a Comment: " comment;\
	git commit -m $$comment;\
	git push origin master
endif

register:
	@python setup.py register

upload:
	@python setup.py sdist upload
	
# clean part
clean:
ifeq ($(CURRENT_OS),Windows)
	@del /Q /S *.bak
	@del /Q /S *.pyc
	@rmdir /Q /S dist
else
	@find . -regex ".*\.\(pyc\|bak\)" | xargs rm
	@rm -rf dist
endif
