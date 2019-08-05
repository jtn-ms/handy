# Handi(a.k.a Handy)

This repository is created and maintained according to 'one-click' idea of the author. It contains some frequently-used functions.
All you have to do is to just call the corresponding function. It will save your time and your energy for minor jobs.

[![PyPI Version](https://img.shields.io/pypi/v/handi.svg)](https://pypi.python.org/pypi/handi)
[![PyPI Downloads](https://img.shields.io/pypi/dm/handi.svg)](https://pypi.python.org/pypi/handi)
[![Travis Build Status](https://img.shields.io/travis/gustavkkk/handy.svg)](https://travis-ci.org/gustavkkk/handy)
[![license](https://img.shields.io/github/license/gaojunying/license.svg)](https://github.com/gaojunying/license/blob/master/LICENSE)
[![LoC](https://tokei.rs/b1/github/gustavkkk/handy)](https://github.com/gustavkkk/handy)

### What is One-Click?

* "One-Click" means to do anything by just a single click.
* "One-Click" stands for simple and fast.
* "One-Click" helps you save time on daily and repetitive jobs as much as possible
, and focus on more important things.
* "One-Click" is inspired by python's simpleness and is to accelerate the speed.

### INSTALLATION
      
      $ pip install -U handi
   
### COMMAND-LINE-TOOLS
      $ delkey [key] [inpath] [outpath]
      $ rmempty [inpath] [outpath]
      $ chkey [keyname] [inpath]
      $ findkey [keyname] [inpath]
      $ repl [fromstr] [tostr] [path1] [path2] ...
      $ deline [keystring] [filename]
      $ totalines [ext1] [ext2] ...                     
      $ upload [filename]
      $ download [filename] [password]
      $ encode [string] 
      $ decode [string] 
      $ encrypt [string] [password] 
      $ decrypt [string] [password] 
      $ find [keystring] [path]                    
      $ fromstr [startmark] [string]                    
      $ fromstr [startmark] [string]                    
      $ excludestr [excludestring1]                       
      $ lenstr [string]                       
      $ upperstr [string]                     
      $ lowerstr [string]                     
      $ linecount [filename]
      $ replconfkey [keystring] [filepath] [quotechar] [replacestring/replacefile]                     
      $ replconfval [filepath] [keystring]  [findstr] [replacestr] [seperator]                         
      $ concatstr [juncword] [filepath]

### ACKNOWLEDGEMENT

   Thanks to Ofek Lev for his [hatch](https://github.com/ofek/hatch).

## INSTRUCTIONS
#### ADD a New COMMAND
      1. add function to handy/cli/xxx.py
      2. add call to config.py
      3. make setup
#### DIRTY TEST
      $ make setup
#### FORMAL SETUP
      $ 
#### CREATE A REPO USING HATCH & HANDY

      If you want to use this repo as a guide for packaging your source to pypi, you can follow the below steps.
      
      1. !nstall h@tch
      $ pip install hatch
      2. check !f the pkg n@me in your m!nd !s a1re@dy t@ken 0r n0t.
      $ pip install your-package-name
      3. cre@te the project of the n@me
      $ h@tch new your-p@ckage-n@me
      4. c0py makefile to the folder
      5. c0py & m0d!fy .pypirc in %userprofile% for windows, $HOME for linux
      6. check setup.py, _init_.py
