import socket

# HOST = '192.168.100.21' #나중에여기 라즈베리파이 호스트 입력
HOST = '192.168.100.15' #세훈이
PORT = 9009 # 라즈베리파이 포트번호 입력

def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' %filename)
            return

        with open('C:\\HC\\videoList\\' + filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)

    print('파일[%s] 전송종료. 전송량 [%d]' %(filename, data_transferred))
