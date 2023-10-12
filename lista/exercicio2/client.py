import socket
HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = s.recv(1024)
    print(msg)
    valor1 =  float(input("digite o valor 1"))
    valor2 =  float(input("digite o valor 2"))
    enviar = str(valor1)+":"+str(valor2)
    s.send(enviar.encode())

    msg2 = s.recv(1024)

    print(msg2)
    
    op = input("")

    s.send(op.encode())

    msg3 = s.recv(1024)

    print(msg3)
    s.close
