import socket
import base64
import sys
# https://stackoverflow.com/questions/36594400/what-is-backlog-in-tcp-connections
BACKLOG = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server = ('192.168.0.13', 5000)

print("Server en %a:%d" % server)

sock.bind(server)
sock.listen(BACKLOG)
conn, address = sock.accept()
print(address, ' se ha conectado')
f = open('recibido.png', 'wb')

# recibo
print('Esperando archivo')
while True:
    data = conn.recv(2048)
    recvImg = base64.b64decode(data)
    if recvImg:
        f.write(recvImg)
    else:
        print('\nRecibido')
        f.close()
        # reenvio
        f_new = open("recibido.png", "rb")
        content = f_new.read()
        print("Empezar a reenviar")
        while content:
            sys.stdout.write('.')
            conn.send(content)
            content = f_new.read()
        print('\nArchivo reenviado')
        break
    sys.stdout.write(".")


conn.close()
# f.close()   
f_new.close()
