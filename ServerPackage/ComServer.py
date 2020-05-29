import socketserver
from ServerPackage.ComClient import getFileFromServer
import parkNumPackage.GeonPark

HOST = '192.168.100.3' #내 컴퓨터 아이피 주소
PORT = 9999 #내 컴퓨터 포트 번호


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        data = data.decode()

        if data is None:
            return
        else:
            getFileFromServer(data)
            parkNumPackage.GeonPark.Main()


def runServer():
    print("========Message 서버 시작=========")

    print("=====파일 서버 종료는 Ctrl + C 를 누르세요.")

    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("=======파일 서버 종료 =========")


runServer()
