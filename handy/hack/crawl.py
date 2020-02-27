import mechanize
from time import sleep

def downloadlink(l):
    f=open(l.text,"w") #perhaps you should open in a better way & ensure that file doesn't already exist.
    br.click_link(l)
    f.write(br.response().read())
    print("%s has been downloaded"%l.text)
    #br.back()

exts=[".zip",".exe",".tar.gz",".rar",".htm",".html",".md"]

def downloadURL(url,path=None):
    #Make a Browser (think of this as chrome or firefox etc)
    br = mechanize.Browser()

    #visit http://stockrt.github.com/p/emulating-a-browser-in-python-with-mechanize/
    #for more ways to set up your br browser object e.g. so it look like mozilla
    #and if you need to fill out forms with passwords.

    # open your site
    br.open(url)

    if not path:
        mark='//'
        path = url[url.find(mark)+len(mark):] if mark in url else url
        if path[-1] is '/': path += 'index.html'
        if '.htm' not in path[-5:]: path += '/index.html'
        filename = path.split('/')[-1]
        dirpath = path[:path.find(filename)]
        import os
        if not os.path.exists(dirpath): os.makedirs(dirpath)

    # save web page
    with open(path,"w") as f:
        f.write(br.response().read()) #can be helpful for debugging maybe

    # filetypes=[".zip",".exe",".tar.gz"] #you will need to do some kind of pattern matching on your files
    # myfiles=[]
    # for l in br.links(): #you can also iterate through br.forms() to print forms on the page!
    #     for t in filetypes:
    #         if t in str(l): #check if this link has the file extension we want (you may choose to use reg expressions or something)
    #             myfiles.append(l)

    # for l in myfiles:
    #     sleep(1) #throttle so you dont hammer the site
    #     downloadlink(l)