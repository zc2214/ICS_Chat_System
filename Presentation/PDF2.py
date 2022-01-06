    if not os.path.exists(des_dir):		
        os.makedirs(des_dir)

    if os.path.exists(src_dir):
        dirs = os.listdir(src_dir)          
        for dirc in dirs:
            if dirc[-3:] == "pdf":               
                pdf_reader = PdfFileReader(open(os.path.join(src_dir, dirc), 'rb'))      
                paper_title = pdf_reader.getDocumentInfo().title                         
                paper_title = str(paper_title)                                        