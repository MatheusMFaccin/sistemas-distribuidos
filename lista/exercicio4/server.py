import socket

def invertString(string):
    return string[::-1]

host = 'localhost'  
port = 12345  


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_socket.bind((host, port))

print(f"Servidor UDP esperando por mensagens em {host}:{port}")


while True:
    data, address = server_socket.recvfrom(1024)  
    mensagem = data.decode('utf-8')
    print(f"Recebido de {address}: ",mensagem)
    mensagem = invertString(mensagem)
    server_socket.sendto(mensagem.encode('utf-8'), (address[0],address[1])) 