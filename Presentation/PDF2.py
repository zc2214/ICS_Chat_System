if not os.path.exists(des_dir):#if no, creat one
    os.makedirs(des_dir)

if os.path.exists(src_dir):
    dirs = os.listdir(src_dir)          
    for dirc in dirs:
        pdf_reader = PdfFileReader(open(os.path.join(src_dir, dirc), 'rb'))     
        paper_title = pdf_reader.getDocumentInfo().title                       
        print("num : %s" % num , paper_title)                                  
        num += 1
        paper_title = str(paper_title)                                          