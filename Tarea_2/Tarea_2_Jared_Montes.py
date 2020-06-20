import re

regex = r"(^[a-zA-Z_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


def check(email):

    if (re.search(regex, email)):
        print("valido Email")

    else:
        print("incalido email")


regex1 = '^\d{10}|\(\d{2,3}\)\d{7,8}|\(\d{2,3}\)[-\s]??\d{3,4}[-\s]??\d{4}$'


def telephone(phone):

    if (re.match(regex1, phone)):
        print("valido")

    else:
        print("invalido")


regex2 = '^[A-ZÑ&]{4}\d{6}(?:[A-Z\d]{3})?$'


def Rfc(money):
    if (re.match(regex2, money)):
        print("valido")

    else:
        print("invalido")


regex3 = '^[A-ZÑ&]{4}\d{6}[HM]{1}[A-ZÑ&]{5}(?:[A-Z\d]{2})?$'

def Curp(clave):
    if (re.match(regex3, clave)):
        print("valido")

    else:
        print("invalido")

if __name__ == '__main__':

    email = "juan@pads.mx"
    check(email)
    email = "juan.ola@pads.com.mx"
    check(email)
    email = "juan_ola@pads.python.com.mx"
    check(email)
    phone = "3311445592"
    telephone(phone)
    phone = "(33) 1144-5594"
    telephone(phone)
    phone = "(331) 144-5595"
    telephone(phone)
    phone = "(33)12345678"
    telephone(phone)
    phone = "(331)2345678"
    telephone(phone)
    money = "CUPÑ800825569"
    Rfc(money)
    clave = "BADD110313HCMLNS09"
    Curp(clave)
