# Se debe crear un modelo de estudiante que herede de Document              ✔
# Utilizar base de datos con nombre 'padts' y coleccion 'estudiantes'       ✔
# Crear método para escritura                                               ✔
#     Se debe ingresar los datos de estudiante como un objeto del modelo.   ✔
# Crear método para lectura                                                 ✔
#     Se debe indicar el estudiante por parámetro                           ✔
#     Se debe regresar un objeto del modelo de estudiante                   ✔
# Crear método para actualización                                           ✔
#     Se debe indicar el estudiante por parámetro                           ✔
#     Se debe retornar el estudiante actualizado                            ✔
# Crear método para eliminar                                                ✔
#     Se debe indicar el estudiante por parámetro                           ✔
#     Se debe retornar un objeto con todos los estudiantes restantes
from mongoengine import *
from rgx import *

connect('Padts')


# Esquema/Modelo
class Estudiantes(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

    def write(self, name, email, password):
        if nom(name) and check(email) and passw(password) == True:
            Estudiantes(name=name, email=email, password=password).save()
            return f'Nombre: {name}\nemail: {email}\npassword: {password}'
        else:
            return 'Revise que los datos sean correctos y no haber dejado espacios sin llenar'

    def read(self, estud):
        if nom(estud) == False:
            return 'Revise que el nombre sea correcto'
        else:
            est = Estudiantes.objects
            for index, p in enumerate(est):
                if p.name == estud:
                    return f'{index + 1} - Nombre: {p.name}\nemail: {p.email}\npassword: {p.password}'
            return 'Estudiante no encontrado'

    def remove(self, stu):
        if nom(stu) == False:
            return 'Revise que el nombre sea correcto'
        else:
            user = Estudiantes.objects(name=stu).first()
            if not user:
                return 'Dato no encontrado'
            else:
                user.delete()
                est = Estudiantes.objects()
                while True:
                    for index, p in enumerate(est):
                        return f'{index + 1} - Nombre: {p.name}\nemail: {p.email}\npassword: {p.password}'


    def updates(self, estu, em, pas):
            user = Estudiantes.objects(name=estu).first()
            if not user:
                return'Dato no encontrado'
            else:
                if nom(estu) and check(em) and passw(pas) == True:
                    Estudiantes.objects(name=estu).modify(upsert=True, new=True, set__email=em, set__password=pas)
                    return f'Nombre: {estu}\nemail: {em}\npassword: {pas}'
                else:
                    return 'Revise que los datos sean correctos y no haber dejado espacios sin llenar'


