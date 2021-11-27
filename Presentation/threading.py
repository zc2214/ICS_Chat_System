from threading import Thread
import file_server

def main():
    Thread(target=file_server.main).start()
    server = Server()
    server.run()