import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from shutil import copy2
from pathlib import Path

def main(path):
    '''
    src_dir = Path(__file__).parent/"papers_oldDir"               #Local folder
    des_dir = Path(__file__).parent/'papers_newDir'               #new folder
    '''
    src_dir = path
    des_dir = src_dir + "/'papers_newDir'"