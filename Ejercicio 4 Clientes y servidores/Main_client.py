import ClienteTcp


if __name__ == '__main__':
    client = ClienteTcp.ClientTCP()
    client.write('stop')  # Para detener el servidor utilizar stop (salir loop)
    client.read()
