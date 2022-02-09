from rest_framework import exceptions


class NegativeAgeError(exceptions.NotAcceptable):
    pass


def my_func(num):
    try:
        if num < 0:
            raise NegativeAgeError
    except NegativeAgeError:
        print("Lesser than 0.")

my_func(-2)