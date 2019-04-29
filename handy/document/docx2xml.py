# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:12:09 2017

@author: Frank
"""

from __future__ import absolute_import

from zipfile import ZipFile
from lxml import etree
import os
import shutil
import sys

filenames = ['[Content_Types].xml', '_rels/.rels', 'word/_rels/document.xml.rels', 'word/document.xml', 'word/theme/theme1.xml', 'word/settings.xml', 'word/fontTable.xml', 'word/webSettings.xml', 'docProps/app.xml', 'docProps/core.xml', 'word/styles.xml']
#filenames += ['docProps/custom.xml']
#filenames += ['word/embeddings/oleObject%d.bin'%index for index in [1,2]]
#filenames += ['word/media/image%d.wmf'%index for index in [1,2]]
#filenames += ['word/footer%d.xml'%index for index in range(1,10)]
#filenames += ['word/header%d.xml'%index for index in [1,2]]
#filenames += ['word/footnotes.xml','word/endnotes.xml','word/numbering.xml']
def xmltree2xml(xmltree,xml_filename,encoding):
    prettyxml = etree.tostring(xmltree,encoding=encoding,pretty_print=True)
    with open(xml_filename,'w+b') as xml_file:
        xml_file.write(prettyxml)    
    
def docx2xml(docx_filename,xml_filename=None,encoding="utf8"):
    if not os.path.exists(docx_filename):
        print('There is no such a file.')
        return
    with open(docx_filename,'r+b') as docx_file:
        xml = ZipFile(docx_file).read('word/document.xml')
        xmltree = etree.fromstring(xml)
        if xml_filename is None:
            xml_filename = os.path.splitext(docx_filename)[0] + '.xml'
        xmltree2xml(xmltree,xml_filename,encoding=encoding)

def docx2xmltree(docx_filename):
    if not os.path.exists(docx_filename):
        print('There is no such a file.')
        return None
    with open(docx_filename,'r+b') as docx_file:
        xml = ZipFile(docx_file).read('word/document.xml')
        xmltree = etree.fromstring(xml)
        return xmltree

# need to be refined
import site
try:
    __path__ = os.path.join(site.getsitepackages()[1],'handy/document')
except AttributeError:
    __path__ = os.getcwd()
    
tmp_path = os.path.join(__path__,'tmp')

def zip2docx(docx_filename):
    if not os.path.exists(tmp_path):
        print('you should copy named "tmp" folder to your distribution directory if you want distribution')
        return
    with ZipFile(docx_filename, "w") as docx_:
        for filename in filenames:
            docx_.write(os.path.join(tmp_path,filename), filename)    

def xmltree2docx(xmltree,docx_filename,encoding="utf8"):
    if not os.path.exists(tmp_path):
        print('you should copy named "tmp" folder to your distribution directory if you want distribution')
        return
    xmltree2xml(xmltree,os.path.join(tmp_path,'word/document.xml'),encoding=encoding)
    zip2docx(docx_filename)
            
def xml2docx(xml_filename,docx_filename=None):
    if not os.path.exists(tmp_path):
        print('you should copy named "tmp" folder to your distribution directory if you want distribution')
        return
    if not docx_filename:
         docx_filename = os.path.splitext(xml_filename)[0] + '.docx'
    shutil.copy(xml_filename, os.path.join(tmp_path,'word/document.xml'))
    zip2docx(docx_filename)

#from docx import Document

from pydocx import PyDocX
def docx2html(docx_filepath,html_filename=None):
    with open(docx_filepath, 'rb') as docx_file:
        html = PyDocX.to_html(docx_file)
        xmltree = etree.fromstring(html)
        prettyxml = etree.tostring(xmltree,pretty_print=True)
        if html_filename is None:
            html_filename =  os.path.splitext(docx_filepath)[0] + '.html'
        with open(html_filename,'w+b') as html_file:
            html_file.write(prettyxml)

import docx
def docx2text(docx_filepath):
    doc = docx.Document(docx_filepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
from handy.document.docx2xml import docx2xml
if __name__ == "__main__":
    docx2xml(sys.argv[1])
    

    