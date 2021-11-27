def download(path=str(Path(__file__).parent / 'user_files' / 'user1')):
    """all files on server are stored in path folder"""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    ftp = ftpconnect()
    for filename in ftp.nlst():
        with open(path / filename, "wb") as f:
            ftp.retrbinary('RETR %s' % filename, f.write)
    ftp.quit()

class GUI:
        def download_for_current_user():
            download(str(Path(__file__).parent / 'user_files' / self.user_name))