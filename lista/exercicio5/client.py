import socket
import threading
HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def recebeMensagem():
    while True:
        
        try:
            client_socket.send("".encode('utf-8'))
            msg = client_socket.recv(1024)
            if not msg:
                print("")
            else:   
                print("\nMensagem recebida: " + msg.decode('utf-8') + "\n")
        except ConnectionResetError:
            print("Conexão encerrada inesperadamente.")
            break
                
def enviaMensagem():
    while True:
        menssagem = input("digite a menssagem que deseja enviar\n")
      
        client_socket.send(menssagem.encode('utf-8'))
        
    
threadEnviaMensagem = threading.Thread(target=enviaMensagem)
threadRecebeMensagem = threading.Thread(target=recebeMensagem)
threadEnviaMensagem.start()
threadRecebeMensagem.start()
