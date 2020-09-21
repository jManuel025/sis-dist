import socket
import base64
import sys 
import cv2
from compara import compara

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('192.168.0.13', 5000)
    
image_coded = None

try:
    f = open("img.png", "rb")
    image_content = f.read()
    imgSent = image_content
    f.close()
    image_coded = base64.b64encode(image_content)
except Exception as e:
    print("Asegúrate de que exista el archivo img.png")
    
if image_coded is not None:
    try:
        sock.connect(server)
        # envío
        while True:
            sock.send(image_coded)
            sock.shutdown(socket.SHUT_WR) 
            print('Archivo enviado')
            break
            
        # recibo
        f_new = open('img2.png', 'wb')
        while True:
            image = sock.recv(2048)
            if image:
                f_new.write(image)
                sys.stdout.write(".")
            else:
                print('\nRecibido')
                break
        f_new.close()

        # compara
        img1 = cv2.imread('img.png', 1)
        img2 = cv2.imread('img2.png', 1)
        similitud = compara(img1, img2)
        if similitud:
            print('Las imagenes son iguales')
        else:
            print('Las imagenes no son iguales')

    except socket.gaierror as e:
        # https://docs.python.org/3/library/socket.html#socket.gaierror
        print(e)
    except Exception as e:
        print(e)
    finally:
        sock.close()
        
