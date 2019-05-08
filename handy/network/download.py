'''
@author:  written by falcon
 
@date: created at 2018.01.30
 
@ref: https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
'''
import os

anaconda_pkg = [
                'https://binstar-cio-packages-prod.s3.amazonaws.com/55d5a2dae850de506e38640b/589b85fffcf1cf11711ec367?response-content-disposition=attachment%3B%20filename%3D%22opencv3-3.1.0-py35_0.tar.bz2%22%3B%20filename%2A%3DUTF-8%27%27opencv3-3.1.0-py35_0.tar.bz2&response-content-type=application%2Fx-tar&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=60&X-Amz-Date=20180130T043040Z&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FQoDYXdzEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDMdfK9a5%2Fah6%2FWCN%2FCK3AwX%2BfEzjgdLiPbuncKSzRf1BJIPztgc5sdea%2Fwe%2BE09Oi860N6RVQOP26bZoRX5OGwofuAWNkIuh3QVUG96jH4ZPThSG4Fxo4EmXdtd65meRGzFwsQTLNBUTNdZ81qaXUFeRc2b1iGQp27xicmT1jjV%2F4vaPJUDBG4AwYTRHkbiofdNSfNICbLacCZRH%2Bsnx6ElNFolfBIYmfEdUBuGctuXf3hOniCIorxTwTO9agv24sWnkDltK6IQ7y1AqnhVopyowZj55LMEBJibrI3lSm9v%2FwXDHskgIc%2FmiBpK0LioF5%2BaDJUWUWmM9bCNtsd6bLpjCJNM3as9RKaZf16nXQaTG5MMRTTA0%2FT2jPiHKX%2Bj7Zg0FFKjaErBqFnCRbU2hmxloPm5N%2BUdVicECXdeXoPFTr33ePL0xSr8qJ4%2ByQnbYlT%2F6Y%2FMQB%2Bihfu%2BCioCwORCdggsNT99Yboevd568Dm8Wu0Iy1jbwq9%2FZimagKKFYJaJ6gjGpK5NaB7%2FK2wD0oO6pd8FtDqsP2xsl8v31M9JXuuTtcm%2BrB1Dd30OBDf8p3WnIefM5vpXIaLJQGYQNinFHG0vkgRooltm%2B0wU%3D&X-Amz-Credential=ASIAJFFMP3DCRB2JSCSQ%2F20180130%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=82c3c4f9c72046c9ae675f0ff757bee5c22a03c010c90b6b627b27c006e72c08',
                ]

lfd_uci_edu_pkgs = [
                    'https://download.lfd.uci.edu/pythonlibs/n1rrk3iq/wcwidth-0.1.5-py2.py3-none-any.whl',
                    ]

def scrape(url='https://www.lfd.uci.edu/~gohlke/pythonlibs/'):
    os.system('curl %s'%url)
    
models = [
       #'https://www.cntk.ai/DataSets/Grocery/Grocery.zip',
       #'https://www.cntk.ai/Models/AlexNet/AlexNet.model',
       'https://cntk.ai/Models/FRCN_Grocery/Fast-RCNN.model',
       #- Visual Object Tagging Tool (VOTT)
       #'http://opencv.jp/opencv-1.0.0_org/docs/papers/camshift.pdf',
       'https://www.cntk.ai/Models/CNTK_Pretrained/AlexNet_ImageNet_CNTK.model',
       'https://www.cntk.ai/Models/Caffe_Converted/AlexNet_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/CNTK_Pretrained/InceptionV3_ImageNet_CNTK.model',
       'https://www.cntk.ai/Models/Caffe_Converted/BNInception_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/CNTK_Pretrained/ResNet18_ImageNet_CNTK.model',
       'https://www.cntk.ai/Models/CNTK_Pretrained/ResNet34_ImageNet_CNTK.model',
       'https://www.cntk.ai/Models/CNTK_Pretrained/ResNet50_ImageNet_CNTK.model',
       'https://www.cntk.ai/Models/CNTK_Pretrained/ResNet20_CIFAR10_CNTK.model',
       'https://www.cntk.ai/Models/CNTK_Pretrained/ResNet110_CIFAR10_CNTK.model',
       'https://www.cntk.ai/Models/Caffe_Converted/ResNet50_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/Caffe_Converted/ResNet101_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/Caffe_Converted/ResNet152_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/Caffe_Converted/VGG16_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/Caffe_Converted/VGG19_ImageNet_Caffe.model',
       'https://www.cntk.ai/Models/FRCN_Grocery/Fast-RCNN_grocery100.model',
       'https://www.cntk.ai/Models/FRCN_Pascal/Fast-RCNN.model',
       'http://dl.dropboxusercontent.com/s/orrt7o6bp6ae0tc/selective_search_data.tgz?dl=0',
       'http://koen.me/research/pub/uijlings-ijcv2013-draft.pdf'
       ]

frcnn_src = [
                'https://github.com/rbgirshick/py-faster-rcnn',
                'https://github.com/rbgirshick/fast-rcnn',#caffe
                'https://github.com/smallcorgi/Faster-RCNN_TF',#tensorlfow
                'https://github.com/azure/ObjectDetectionUsingCntk',#cntk
            ]

frcnn_tutorial = [
                    'https://www.yumpu.com/en/document/view/55251653/fast-r-cnn-object-detection-with-caffe',
                ]
nupkgs = [
        'https://az320820.vo.msecnd.net/packages/cntk.cpuonly.2.1.0.nupkg',
        'https://az320820.vo.msecnd.net/packages/cntk.gpu.2.1.0.nupkg',
        'https://az320820.vo.msecnd.net/packages/cntk.uwp.cpuonly.2.1.0.nupkg',
        ]

ptvs = [
        'https://codeload.github.com/Microsoft/PTVS/zip/v2.2.2',
        'https://codeload.github.com/Microsoft/PTVS/zip/v2.2.6',
        'https://ptvs.azureedge.net/download/PTVS%202.2.2%20VS%202013.msi',
        'https://ptvs.azureedge.net/download/PTVS%202.2.2%20VS%202015.msi',
        'https://ptvs.azureedge.net/download/PTVS%20ML%202.2.2.vsix',
        'https://ptvs.azureedge.net/download/PTVS%20Samples%202.2.2.vsix',
        ]

import os
import urllib
try:#if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
    python3 = True
except ImportError:#else:
    import urllib2
    import urlparse
    python3 = False
import requests
modes = ['requests','wget','urllib','urllib2']

def download_file(url, dest=None):
    """ 
    Download and save a file specified by url to dest directory,
    """
    u = urllib2.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    if not filename:
        filename = 'downloaded.file'
    if dest:
        filename = os.path.join(dest, filename)

    with open(filename, 'wb') as f:
        meta = u.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print("Downloading: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = "{0:16}".format(file_size_dl)
            if file_size:
                status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
            status += chr(13)
            print(status)
        print()

    return filename

def get_fileinfo(url):
    u = urllib2.urlopen(url)
    file_name = url.split('/')[-1]
    meta = u.info()
    meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
    meta_length = meta_func("Content-Length")
    file_size = None
    if meta_length:
        file_size = int(meta_length[0])
    return file_name,file_size

def download_urllib(url,filename=None):
    if not filename:
        filename = url.split('/')[-1]
    import sys
    if sys.version_info >= (3,):
        urllib2.urlretrieve (url, filename)
    else:
        urllib.urlretrieve (url, filename)

def download_urllib2(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
    meta_length = meta_func("Content-Length")
    file_size = None
    if meta_length:
        file_size = int(meta_length[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))
    
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
    
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)
    
    f.close()

from tqdm import tqdm
def download_requests(url,filename=None):
    if not filename:
        filename = url.split('/')[-1]
    response = requests.get(url, stream=True)
    filesize = len(response.content)
    print(filesize)
    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
            
def download_system(url):
    file_name,file_size = get_fileinfo(url)
    if os.path.exists(file_name) and file_size == os.path.getsize(file_name):
        return
    response = os.system('wget --no-check-certificate %s'%url)#os.system('curl %s'%url)
    if os.path.getsize(file_name) != file_size:
        os.remove(file_name)
    print(response)
    return

import wget
import time
from functools import wraps
def profile(func):
    @wraps(func)
    def inner(*args):
        print(func.__name__, ": starting")
        start = time.time()
        ret = func(*args)
        end = time.time()
        print(func.__name__, ": {:.2f}".format(end - start))
        return ret
    return inner

def do_nothing(*args):
    pass

@profile
def download_wget(url,useBar=False):
    if useBar:
        response = wget.download(url, out='/tmp/')
    else:
        response = wget.download(url, out='/tmp/', bar=do_nothing)
    print(response)
    return response

 ##### onedrive ####################################
# import onedrivesdk								#
# redirect_uri = 'http://localhost:8080/'			#
# client_id='aef8dc46-82c7-4c55-94fb-bc578b66ccd3'	#
# client_secret='reyjZMS8!~wxcTWJR2793?|'			#
 ###################################################
 
def download(url,mode='system'):
    if 'system' in mode:
        download_system(url)
    elif 'wget' in mode:
        download_wget(url)
    elif 'requests' in mode:
        download_requests(url)
    elif 'urllib' in mode:
        download_urllib(url)
    elif 'urllib2' in mode:
        download_urllib2(url)

def download_onedrive(filename):
	pass
def upload_onedrive(filename):
	pass
def main():
    for url in models:
        download(url,'system')
        
if __name__ == "__main__":
    main()   
