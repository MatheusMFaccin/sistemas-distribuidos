import socket
import threading
HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def operacao(escolha):
    quantia = ""
    if escolha == "1":
        quantia = float(input("\ndigite a quantia que deseja sacar \n"))
        return str(quantia)+":1"
    elif escolha == "2":
        quantia = float(input("\n digite a quantia que deseja depositar \n"))
        return str(quantia)+":2"
    
    elif escolha == "3":
        quantia = "deposito"
        return quantia+":3"
    else:
        quantia =  ""
        return quantia+":4"
    
def recebeMensagem():
    msg = ""
    client_socket.send(msg.encode('utf-8'))
    while True:
        msg = client_socket.recv(1024)
        print("\n"+msg.decode('utf-8')+"\n")
                
def enviaMensagem():
    while True:
        escolha = input("digite 1 se deseja sacar o dinheiro digite 2 se deseja depositar ou digite 3 se deseja consultar o saldo\n")
        mensagem  = operacao(escolha)
        client_socket.send(mensagem.encode('utf-8'))
        
    
threadEnviaMensagem = threading.Thread(target=enviaMensagem)
threadRecebeMensagem = threading.Thread(target=recebeMensagem)
threadEnviaMensagem.start()
threadRecebeMensagem.start()



