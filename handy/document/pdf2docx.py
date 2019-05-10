# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:12:09 2017

@author: Frank
"""

from __future__ import absolute_import

import os
import platform
if platform == "win32":
    import comtypes.client
    from win32com.client import Dispatch

    WORD = 'Word.Application'
    wdFormatPDF = 17#https://msdn.microsoft.com/en-us/VBA/Word-VBA/articles/wdsaveformat-enumeration-word
    wdFormatDocx = 12

    def pdf2docx(pdf_filepath,docx_filepath=None):
        pdf_filepath = os.path.abspath(pdf_filepath)
        if not os.path.exists(pdf_filepath):
            print('There is no such a file.')
            return
        word = Dispatch(WORD)
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(pdf_filepath)
        if not docx_filepath:
            docx_filepath = pdf_filepath.replace(".pdf", r".docx")
        else:
            docx_filepath = os.path.abspath(docx_filepath)
        doc.SaveAs2(docx_filepath, FileFormat=wdFormatDocx)
        doc.Close()
        word.Quit()

    def docx2pdf(docx_filepath,pdf_filepath=None):
        docx_filepath = os.path.abspath(docx_filepath)
        if not os.path.exists(docx_filepath):
            print('There is no such a file.')
            return
        word = comtypes.client.CreateObject(WORD)
        word.Visible = False
        doc = word.Documents.Open(docx_filepath)
        if not pdf_filepath:
            pdf_filepath = docx_filepath.replace(".docx", r".pdf")
        else:
            pdf_filepath = os.path.abspath(pdf_filepath)
        #doc.SaveAs2(pdf_filepath, FileFormat=wdFormatPDF)
        doc.SaveAs(pdf_filepath, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()

    def opendocument(filepath):
        filepath = os.path.abspath(filepath)
        if not os.path.exists(filepath):
            print('There is no such a file.')
            return
        word = Dispatch(WORD)
        word.Visible = True
        word.DisplayAlerts = 0    
        word.Documents.Open(filepath)

    def doc2docx(doc_filepath,docx_filepath=None):
        #https://social.msdn.microsoft.com/Forums/en-US/a4f00910-cb6e-4861-bf96-97b0cfc6cf8f/convert-word-files-from-doc-to-docx-using-python?forum=worddev
        doc_filepath = os.path.abspath(doc_filepath)
        if not os.path.exists(doc_filepath):
            print('There is no such a file.')
            return
        word = Dispatch(WORD)
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(doc_filepath)
        if not docx_filepath:
            docx_filepath = doc_filepath.replace(".doc", r".docx")
        else:
            docx_filepath = os.path.abspath(docx_filepath)
        #print(docx_filepath)
        #doc.SaveAs2(docx_filepath, FileFormat=wdFormatDocx)
        doc.SaveAs(docx_filepath, FileFormat=wdFormatDocx)
        doc.Close()
        word.Quit()
    '''
    import subprocess
    def doc2docx_under_test(doc_filepath,docx_filepath=None):
        subprocess.call('soffice --headless --convert-to docx'.format(doc_filepath), shell=True)#(['soffice', '--headless', '--convert-to', 'docx', doc_filepath])
        
    def pdf2docx_under_test(pdf_filepath,docx_filepath=''):
        subprocess.call('lowriter --invisible --convert-to doc "{}"'
                        .format(pdf_filepath), shell=True)

    def pdf2docx_dir_under_test(path='/my/pdf/folder'):
        for top, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith('.pdf'):
                    abspath = os.path.join(top, filename)
                    subprocess.call('lowriter --invisible --convert-to doc "{}"'
                                    .format(abspath), shell=True)
                    
    '''