# detect operating system
ifeq ($(OS),Windows_NT)
    CURRENT_OS := Windows
else
    CURRENT_OS := $(shell uname -s)
endif

up:	clean
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

clean:
ifeq ($(CURRENT_OS),Windows)
	@del /Q /S *.bak *.pyc
else
	@find . -regex ".*\.\(pyc\|bak\)" | xargs rm
endif
