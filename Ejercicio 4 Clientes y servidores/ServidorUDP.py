# Debe asignar puerto en el constructor
## El constructor contiene el procedimiento para recibir paquetes
# ***Debe tener un método para escribir con un parámetro para el mensaje y otro con las dirección (ip +puerto)
## Debe tener un método para leer que retorne el mensaje y la dirección (ip + puerto)
import socket as s


class ServidorUdp:

    def __init__(self, addr):
        self.socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.socketServidor.bind(addr)  # aqui se puede asignar la dirección (ip +puerto) por parametro
        self.data, self.addrs = self.socketServidor.recvfrom(1024)

    def read(self):
        return f'recibi un mensaje: {self.data} de {self.addrs}'

    def write(self, msg):
        self.socketServidor.sendto(msg.encode(), self.addrs)  # ***la diereccion ip es la misma pero el puerto no!
        self.socketServidor.close()                           # ***No se puede asignar dirección (ip +puerto)
