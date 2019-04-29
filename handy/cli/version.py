import sys
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file: return os.path.join(root, file)

msg_help = "Written by junying, 2019-04-29 \
            \nUsage: version [path]  \
            \nDefault: version ."

def main():
    if len(sys.argv) < 2: dirpath='.'
    else: dirpath=sys.argv[1]
    filepath = find('version',dirpath)
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('__version__') or line.startswith('_version_') or line.startswith('version'):
                version = line.strip().split('=')[1].strip(' \'"')
                print(version); return
    print('not found!')