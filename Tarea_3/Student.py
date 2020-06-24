
class Students:
    __name = ''
    __email = ''
    __password = ''

    def get_student(self):
        return self.__name, self.__email, self.__password

    def set_student(self, name1, email1, password1):
        self.__name = name1
        self.__email = email1
        self.__password = password1




