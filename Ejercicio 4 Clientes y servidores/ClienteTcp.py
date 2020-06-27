# Dede realizar la conexión en el constructor
# Debe tener un método para escribir con un parámetro para el mensaje
# Debe tener un método para leer que retorne el mensaje

import socket as s
ip = '127.0.0.1'
port = 35481


class ClientTCP:

    def __init__(self):
        self.client = s.socket()
        self.client.connect((ip, port))

    def write(self, msg):
        byte1 = msg.encode()
        self.client.send(byte1)

    def read(self):
        while True:
            data = self.client.recv(1024)
            print(data)

            if data == b'':
                print('conexion cerrada')
                break
        self.client.close()


