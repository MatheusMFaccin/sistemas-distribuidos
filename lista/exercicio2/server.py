import socket

def soma(valor1,valor2):
    return valor1+valor2
def sub(valor1,valor2):
    return valor1-valor2
def mult(valor1,valor2):
    return valor1*valor2
def div(valor1,valor2):
    return valor1/valor2


HOST = 'localhost'
PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen(1)

conn, adrr = s.accept()

dicionario = {'+':soma,'-':sub,'*':mult,'/':div}


conn.send("envie os valores que deseja fazer as operacoes".encode())

msg = conn.recv(1024)
msg = msg.decode()
print(msg)
valor1,valor2 = msg.split(":")
print(valor1,"  ",valor2)

conn.send("digite a operação que deseja fazer (  +  -  *  / )".encode())

operacao = conn.recv(1024)
operacao = operacao.decode()
enviar = "resposta: "+str(dicionario[operacao](float(valor1),float(valor2)))
conn.send(enviar.encode())
conn.close()
