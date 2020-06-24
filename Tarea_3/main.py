import Student
import Studentio

if __name__ == '__main__':
    #  Obj de la clase estudiante (name, email, password)
    Student_obj1 = Student.Students()
    Student_obj1.set_student('Jared', 'Jaredstudents@example.com', '12345')
    Student_obj2 = Student.Students()
    Student_obj2.set_student('Orlando', 'Orlandostudents@example.com', '56789')
    Student_obj3 = Student.Students()
    Student_obj3.set_student('Marco', 'MArco_students@example.com', '1234asd')
    Student_obj4 = Student.Students()
    Student_obj4.set_student('Yolanda', 'Yolandastudents@example.com', 'Yola1234')
    Student_obj5 = Student.Students()
    Student_obj5.set_student('Maria', 'Maria.students@example.com', 'Mari4567')
    Student_objextra = Student.Students()  # obj extra para update
    Student_objextra.set_student('Josue', 'Josue.students@example.com', 'josue1985')
    #  Shelve db
    Studentio.savestdents(Student_obj1.get_student(), Student_obj2.get_student(),
                          Student_obj3.get_student(), Student_obj4.get_student(),
                          Student_obj5.get_student())
    Studentio.readstudents()
    Studentio.updatestudents(Student_objextra.get_student())
    Studentio.readstudents()
    #  pickle db
    Studentio.savestdentp(Student_obj1.get_student(), Student_obj2.get_student(),
                          Student_obj3.get_student(), Student_obj4.get_student(),
                          Student_obj5.get_student())
    Studentio.readstudentp()
    Studentio.updatestudentp(Student_objextra.get_student())
    Studentio.readstudentp()

