# Debe asignar puerto en el constructor
# El constructor contiene el procedimiento para aceptar las conexiones
# Debe tener un método para escribir con un parémetro para el mensaje
# Debe tener un método para leer que retorne el mensaje

import socket as s

ip = '127.0.0.1'
port = 35481


class ServerTCP:

    def __init__(self):
        self.serverSocked = s.socket()
        self.serverSocked.bind((ip, port))
        self.serverSocked.listen()
        (self.clientecon, self.clienteaddr) = self.serverSocked.accept()  # acepta conexion
        self.data = self.clientecon.recv(1024)  # recivo paquedes de la conexion

    def read(self):
        return self.data

    def write(self, msg):
        while True:
            if self.data != b'':
                msg2 = msg.encode()
                self.clientecon.send(msg2)

                ms2 = 'se cierra la conexion'
                msg2byte = ms2.encode()
                self.clientecon.send(msg2byte)

                self.clientecon.close()  # cerrar conexion
                self.serverSocked.close()
                break
