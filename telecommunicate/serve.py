from socket import  *

def communicate():
    tcp_server = socket(AF_INET,SOCK_STREAM)
    address = ('',8000)
    tcp_server.bind(address)

    tcp_server.listen(128)  

    client_socket, clientAddr = tcp_server.accept()

    from_client_msg = client_socket.recv(1024)
    print("接收的数据：",from_client_msg.decode("gbk"))
    return client_socket

def resend(data,client_socket):
    client_socket.send(data.encode("gbk"))


if __name__ == "__main__":

    
    while True:
        client_socket=communicate()
        context = input("请输入要发送的内容：")
        resend(context,client_socket)
