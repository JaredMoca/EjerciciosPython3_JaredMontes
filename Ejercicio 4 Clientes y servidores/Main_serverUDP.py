import ServidorUDP

if __name__ == '__main__':

    msg = 'server-hola'
    addr = '127.0.0.1', 12345
    while True:
        ServerUd = ServidorUDP.ServidorUdp(addr)
        print(ServerUd.read())
        ServerUd.write(msg)
        if ServerUd.data == b'stop':  # se detiene el servidor
            break
