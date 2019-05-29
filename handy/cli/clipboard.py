import os, sys
    
def pbcopy():
    os.system("xclip -selection clipboard")
    
def pbpaste():
    os.system("xclip -selection clipboard -o")
