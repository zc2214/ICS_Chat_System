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
    num = 0

    if not os.path.exists(des_dir):		#if no, creat one
        os.makedirs(des_dir)

    if os.path.exists(src_dir):
        dirs = os.listdir(src_dir)          
        for dirc in dirs:
            if dirc[-3:] == "pdf":               #For every pdf in folder
                pdf_reader = PdfFileReader(open(os.path.join(src_dir, dirc), 'rb'))      #Open and create a pdf file
                paper_title = pdf_reader.getDocumentInfo().title                         #Get the title                                  # Show progress
                num += 1
                paper_title = str(paper_title)                                           #Title as str
        
                if paper_title.find('/') != -1:       #Error handling
                    new_paper_title = paper_title.replace('/','_')
                    paper_title = new_paper_title
                    copy2(os.path.join(src_dir, dirc), os.path.join(des_dir, paper_title) + '.pdf')
                else:
                    copy2(os.path.join(src_dir, dirc), os.path.join(des_dir, paper_title) + '.pdf')
        
        else:
            print("Error")

if __name__ == "__main__":
    main()
