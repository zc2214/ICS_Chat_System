from pathlib import Path
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
def main():
    authorizer = DummyAuthorizer()
    # Now stored in local file folder
    # "/Users/jameschen/Desktop/" "D:\upload"
    home_path = Path(__file__).parent / 'files'
    home_path.mkdir(parents=True, exist_ok=True) # make new folder, to store the file
    authorizer.add_user("Admin", "Admin", str(home_path), perm='elradfmwM')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('0.0.0.0', 8888), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()