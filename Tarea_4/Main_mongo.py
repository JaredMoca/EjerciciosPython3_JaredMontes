import Mongo

if __name__ == '__main__':
    est = Mongo.Estudiantes()
    name = ['angela', 'mario', 'jose']  # objs
    email = ['angela@example.com', 'mario@example.com', 'jose@example.com']  # objs
    password = ['12345', 'mari123', 'pepe1234']  # objs
    est.write(name, email, password)  # tener cuidado ya que escribe en cada ejecucio
    print(est.read('mario'))  # lee a mario
    print(est.remove('angela'))  # elimina a mario
    print(est.updates('jose', 'pepe@example.com', 'jose1234'))
         # (Nombre-de-estudiante-a-actualizar, nuevo-correo, nueva-contraseña)