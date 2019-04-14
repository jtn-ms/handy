# Handi(a.k.a Handy)

This repository is created and maintained according to 'one-click' idea of the author. It contains some frequently-used functions.
All you have to do is to just call the corresponding function. It will save your time and your energy for minor jobs.

[![license](https://img.shields.io/github/license/gaojunying/license.svg)](https://github.com/gaojunying/license/blob/master/LICENSE)

### DEFINITION: One-Click

* "One-Click" means to do anything by just a single click.
* "One-Click" stands for simple and fast.
* "One-Click" helps you save time on daily and repetitive jobs as much as possible
, and focus on more important things.
* "One-Click" is inspired by python's simpleness and is to accelerate the speed.

### INSTALLATION
      
      $ pip install -U handi

### FUNCTIONS 

   * conversion

    -docx2xml

    -list2txt

    -dict2json

   * compression

    ...
    
### USAGES

      $ python
      >>>from handy.docx2xml import docx2xml
      >>>docx2xml('xxx.docx')

### LICENSE - [MIT License](https://choosealicense.com/licenses/mit)
   
### ACKNOWLEDGEMENT

   Thanks to Ofek Lev for his [hatch](https://github.com/ofek/hatch).
  
### TIP - FOR CREATING A REPO USING HATCH & HANDY

      If you want to use this repo as a guide for packaging your source to pypi, you can follow the below steps.
      
      1. !nstall h@tch
      $ pip install hatch
      2. check !f the pkg n@me in your m!nd !s a1re@dy t@ken 0r n0t.
      $ pip install your-package-name
      3. cre@te the project of the n@me
      $ h@tch new your-p@ckage-n@me
      4. c0py .bat files to the folder
      5. c0py & m0d!fy .pypirc in %userprofile% for windows, $HOME for linux
      6. check setup.py, _init_.py
