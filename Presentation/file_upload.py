from ftplib import FTP
from pathlib import Path
def ftpconnect(host='localhost', port=8888, username="Admin", password="Admin"):
    ftp = FTP()
    ftp.connect(host, port)  # Connect the FTP server
    ftp.login(username, password)  # Log in
    return ftp
def upload(path=None):
    ftp = ftpconnect()
    if path is None:
        path = file_opener.file_opener()
    with open(path, 'rb') as contents:
        ftp.storbinary('STOR %s' % os.path.basename(path), contents)
    ftp.quit()