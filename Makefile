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
GITHUB_ACCOUNT = gustav0125@outlook.com
GITHUB_USER_NAME = gustavkkk
GITHUB_PASSWORD = gustavko0125

login:
	git config --global user.email "$(GITHUB_ACCOUNT)"
	git config --global user.name "$(GITHUB_USER_NAME)"
	git remote set-url origin https://$(GITHUB_USER_NAME):$(GITHUB_PASSWORD)@github.com/gustavkkk/handy.git

up: clean
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

copy:
ifeq ($(CURRENT_OS),Windows)
	@copy .pypirc %USERPROFILE%
else
	@cp .pypirc $HOME
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
