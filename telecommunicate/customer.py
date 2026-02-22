from socket import *


def communicate(ip):
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    serve_ip = ip
    serve_port = 8000  #端口，比如8000
    tcp_socket.connect((serve_ip,serve_port))
    return tcp_socket

def content(send_data, tcp_socket):
    send_data = str(send_data)
    tcp_socket.send(send_data.encode("gbk")) 
    from_server_msg = tcp_socket.recv(1024)
    print(from_server_msg.decode("gbk"))  
    tcp_socket.close()

if __name__ == "__main__":
    ip = input("请输入服务器的ip地址：")
    
    while True:
        tcp_socket=communicate(ip)
        context = input("请输入要发送的内容：")
        content(context,tcp_socket)