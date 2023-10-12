import socket
HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen()

conn, adrr = s.accept()

class Banco:
    def __init__(self) :
        self.saldo = 0
        
    def saque(self, quantia):
        self.saldo -= quantia
    def deposito(self,quantia):
        self.saldo += quantia
    def consulta(self):
        return self.saldo
    
contaBanco = Banco()
def operacao(menssagem):
    quantia, escolha = menssagem.split(":")
    print("escolha: ",escolha)
    if escolha == "1":
        contaBanco.saque(float(quantia))
        return "quantia sacada"
    elif escolha == "2":
        contaBanco.deposito(float(quantia))
        return "quantia depositada"
    elif escolha == "3":
        
        return str(contaBanco.consulta())
    else :
        return "opção invalida"
with conn:
    contaBanco = Banco()
    
    while True:
        
        data = conn.recv(1024)
        menssagem = data.decode('utf-8')
        print(menssagem)
        resposta = operacao(menssagem)
        conn.send(resposta.encode('utf-8'))
    