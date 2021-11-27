import os
from PyPDF2 import  PdfFileReader
from shutil import copy2
from pathlib import Path

src_dir = Path(__file__).parent/"papers_oldDir"               #Local folder
des_dir = Path(__file__).parent/'papers_newDir' 