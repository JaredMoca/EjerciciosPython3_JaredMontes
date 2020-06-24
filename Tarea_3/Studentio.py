import shelve
import pickle


def savestdents(obj1, obj2, obj3, obj4, obj5):
    database = shelve.open("Studentio.db")
    student = [obj1, obj2, obj3, obj4, obj5]
    database['students'] = student
    database.close()


def readstudents():
    var = shelve.open("Studentio.db")
    print("Lista shelve:", var['students'])
    var.close()


def updatestudents(val):
    var = shelve.open("Studentio.db", writeback=True)

    des = str(input("Desea eliminar un elemento de la lista"))
    if des == 'si':
        dele = int(input("Seleccione un el elemento de la lista que desea eliminar"))
        var['students'].pop(dele)  # elimina un obj
    else:
        print('no se elimino ningun elemento')

    var['students'].append(val)  # Agrega un nuevo obj
    print('Lista actualizada shelve:')

    var.sync()

    var.close()


def savestdentp(obj1, obj2, obj3, obj4, obj5):
    emp = {'1':obj1, '2':obj2, '3':obj3, '4':obj4, '5':obj5}
    pickling_on = open("studentio", "wb")
    pickle.dump(emp, pickling_on)
    pickling_on.close()


def readstudentp():
    pickle_off = open("studentio", "rb")
    emp = pickle.load(pickle_off)
    pickle_off.close()
    print("pickle", emp)


def updatestudentp(val):
    pickle_off = open("studentio", "rb")
    mydict = pickle.load(pickle_off)
    mydict.update({'ext': val})
    output = open('studentio', 'wb')
    pickle.dump(mydict, output)
    print('Lista actualizada pickle:')
    output.close()


