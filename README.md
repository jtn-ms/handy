# Handi(a.k.a Handy)

Legacy Commands & Utilities

[![PyPI Version](https://img.shields.io/pypi/v/handi.svg)](https://pypi.python.org/pypi/handi)
[![PyPI Downloads](https://img.shields.io/pypi/dm/handi.svg)](https://pypi.python.org/pypi/handi)
[![Travis Build Status](https://img.shields.io/travis/gustavkkk/handy.svg)](https://travis-ci.org/gustavkkk/handy)
[![license](https://img.shields.io/github/license/gaojunying/license.svg)](https://github.com/gaojunying/license/blob/master/LICENSE)
[![LoC](https://tokei.rs/b1/github/gustavkkk/handy)](https://github.com/gustavkkk/handy)

### INSTALLATION
```
$ pip install -U handi
```   
### COMMAND-LINE-TOOLS
#### 1. Basic Utility
```
[public ip]
$ pubip
$ 143.87.25.158

[private ip]
$ prvip
$ 192.168.10.121

[wifi password]
$ sudo wifipass
$ /etc/NetworkManager/system-connections/My-Office:psk=12345678...

[gps]
$ gps
$ [22.7702, 112.9578]

[timer]
$ timer cp 1.iso ../
$ 3 seconds

[encode]
$ encode [string]
$ encode 12345678
$ 3132333435363738

[decode]
$ decode [string]
$ decode 3132333435363738
$ 12345678

[encrypt]
$ encrypt [string] [password] 
$ encrypt "Nothing is Unlimited." 12345678
$ gAAAAABeIA9OWhfmu6U97CoCdKj0LctEHfs4biG3ts-XULYPR98p1nQ6XKGmW-7D3wIGAWiTvtN73heuO7L7-QLwQZJtPv9qD_kCcofBfJ6UJ--pKcQ8tqY=

[decrypt]
$ decrypt [string] [password]
$ decrypt gAAAAABeIA9OWhfmu6U97CoCdKj0LctEHfs4biG3ts-XULYPR98p1nQ6XKGmW-7D3wIGAWiTvtN73heuO7L7-QLwQZJtPv9qD_kCcofBfJ6UJ--pKcQ8tqY= 12345678
$ Nothing is Unlimited.

[strong remove]
$ srm [repeats] [filename]
$ srm 15 accounts.txt

[shutdonw]
$ boo

[terminal clear]
$ cls

[replace]
$ repl [fromstr] [tostr] [path1] [path2] ...
$ repl junying frank accounts.txt

[statistics]
$ hash
>>hits    command
   1    /usr/bin/which
   1    /usr/local/bin/ipinfo
   4    /usr/local/bin/version
   1    /usr/local/bin/prvip
   6    /usr/local/bin/timer
   3    /usr/local/bin/srm
   2    /usr/local/bin/oneline
   1    /usr/local/bin/sumup
   1    /bin/rm
   1    /usr/bin/vim
   1    /usr/local/bin/cls
   1    /usr/bin/touch
   1    /usr/bin/sudo
   1    /usr/local/bin/rmlnno
  11    /usr/local/bin/mac
   1    /usr/local/bin/printkey
   3    /bin/ls
   1    /usr/local/bin/gps
```
#### 2. Code Management
```
[totalines]
$ totalines [ext1] [ext2] ...
$ totalines py go cpp h java
$ 124535

[git commit]
$ commit
```
#### 3. Text Handling
```
[findstr] 
$ findstr [keystring] [path]

[column]
$ echo Time Machine|column 2
$ Machine

[row]
$ cat accounts.txt|row 2
$ frank     9980

[sumup]
$ sumup [filename]
$ cat accounts.txt|column 2|sumup
$ 1199899.0125

[fromstr]
$ fromstr [startmark] [string]
$ echo Nothing Lasts.|fromstr "Nothing "
$ lasts.

[endstr]
$ endstr [endstring] [string]
$ echo Nothing lasts.|fromstr "Nothings " |endstr .
$ Lasts

[excludestr]
$ excludestr [excludestring1]
$ echo abcdEFG|excludestr EFG
$ abcd

[lenstr]
$ lenstr [string]
$ lenstr 123456789
$ 9

[upperstr]
$ upperstr [string]
$ upperstr gustavKo
$ GUSTAVKO

[lowerstr]
$ lowerstr [string]
$ lowerstr ABcD
$ abcd

[linecount]
$ linecount [filename]
$ linecount accounts.list
$ 14273

[concastr]
$ concatstr [juncword] [filepath]
$ concatstr , 1 2 3 4 5
$ 1,2,3,4,5

[delete specific lines in file]
$ deline [keystring] [filename]
$ deline junying accounts.txt
```

#### JSON Handling
```
$ chkey [keyname] [inpath]
$ delkey [key] [inpath] [outpath]
$ findkey [keyname] [inpath]
$ printkey [keyname] [inpath] [subkey1] [subkey2]
$ replconfval [filepath] [keystring]  [findstr] [replacestr] [seperator]
$ replconfkey [keystring] [filepath] [quotechar] [replacestring/replacefile]
$ rmempty [inpath] [outpath]
```
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
      $ make install
### [RST EDIT](http://rst.ninjs.org/#)
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
