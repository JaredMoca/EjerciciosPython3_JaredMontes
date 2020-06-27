# Debe tener un método para escribir con un parametro para el mensaje y otro con la dirección(ip + puerto)
# Debe tener un método para leer que retorne el mensaje y la dirección(ip + puerto)
import socket as s


class ClienteUdp:

    def __init__(self):
        self.client = s.socket(s.AF_INET, s.SOCK_DGRAM)

    def write(self, addr, msg):
        self.client.sendto(msg.encode(), addr)

    def read(self):
        data, addrs = self.client.recvfrom(1024)
        return f'recibdo: {data} de {addrs}'











