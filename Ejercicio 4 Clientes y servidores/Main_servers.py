import ServidorTcp


if __name__ == '__main__':
    while True:
        Server = ServidorTcp.ServerTCP()
        print(f'reibi un mensaja: {Server.read()}')
        Server.write('servidor en buen estado')
        if Server.read() == b'stop':  # se detiene el servidor
            print('servidor detenido')
            break
