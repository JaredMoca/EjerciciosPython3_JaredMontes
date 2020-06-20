
class Figure:
    Base = 0  # atributos
    Altura = 0

    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura

    def perimeter(self):  # polimorfismo
        pass

    def area(self):  # herencia
        ar = self.Base * self.Altura
        return ar


class Rectangle(Figure):

    def __init__(self, Base, Altura):
        super().__init__(Base, Altura)

    def perimeter(self):  # polimorfismo
        perimetro = self.Base * 2 + self.Altura * 2
        return perimetro


class Triangle(Figure):

    def __init__(self, Base, Altura):
        super().__init__(Base, Altura)

    def area(self):
        ar = (self.Base * self.Altura) / 2
        return ar

    def perimeter(self):  # polimorfismo
        perimetro = self.Base * 3
        return perimetro


Triangle_obj = Triangle(2, 2)
res_area_T = Triangle_obj.area()
print(f'Area Triangulo: {res_area_T}')
res_peri_T = Triangle_obj.perimeter()
print(f'Perimetro Triangulo: {res_peri_T}')

Rectangle_Obj = Rectangle(5, 8)
res_area_R = Rectangle_Obj.area()
print(f'Area Rectangulo: {res_area_R}')
res_peri_R = Rectangle_Obj.perimeter()
print(f'Perimetro Rectangulo: {res_peri_R}')


class Student:
    __name = ''
    __email = ''
    __password = ''

    def get_student(self):
        return self.__name, self.__email, self.__password

    def set_student(self, name1, email1, password1):
        self.__name = name1
        self.__email = email1
        self.__password = password1


Student_obj = Student()
Student_obj.set_student('Jared', 'Jared.montes@example.com', '123')
print(Student_obj.get_student())

