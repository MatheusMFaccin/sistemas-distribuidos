import socket
import threading
HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen()

conn, adrr = s.accept()


    
def recebeMensagem():
    
    while True:
        
        try:
            conn.send("".encode('utf-8'))
            msg = conn.recv(1024)
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
        
        conn.send(menssagem.encode('utf-8'))
        
with conn:
    while True:       
        threadEnviaMensagem = threading.Thread(target=enviaMensagem)
        threadRecebeMensagem = threading.Thread(target=recebeMensagem)
        threadEnviaMensagem.start()
        threadRecebeMensagem.start()
