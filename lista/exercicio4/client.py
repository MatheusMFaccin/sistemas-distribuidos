import socket
import threading
import queue

server_host = '127.0.0.1'  
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message_queue = queue.Queue()


def recebendoMenssagem():
    client_socket.sendto(b"", (server_host, server_port))
    while True:
        data = client_socket.recv(1024)
        mensagem = data.decode('utf-8')
        print(f"Recebido: ",mensagem)


def enviandoMenssagendo():
    while True:
        message = input("Digite uma mensagem para enviar ao servidor: ")
        message_queue.put(message)
        client_socket.sendto(message.encode('utf-8'), (server_host, server_port))
        



thread = threading.Thread(target=recebendoMenssagem)
thread2 = threading.Thread(target=enviandoMenssagendo)

thread2.start()
thread.start()




    