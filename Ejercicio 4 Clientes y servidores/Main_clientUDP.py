import ClienteUDP

if __name__ == '__main__':
    addr = '127.0.0.1', 12345
    msg = 'stop'  # utilizar stop para apagar servidor (salir loop)
    clientud = ClienteUDP.ClienteUdp()
    clientud.write(addr, msg)
    print(clientud.read())
