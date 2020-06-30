import re

regex = r"(^[a-zA-Z_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


def nom(nam):

    if (re.match(regex1, nam)):
        return True

    else:
        return False


regex2 = '^[a-zA-Z0-9-@#$%^&-+=()\s]+$'


def check(email):

    if (re.search(regex, email)):
        return True

    else:
        return False


regex1 = '^[a-zA-Z\s]+$'


def passw(pas):
    if (re.match(regex2, pas)):
        return True

    else:
        return False


