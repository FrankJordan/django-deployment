from django import template

register = template.Library


def cut(value, arg):
    """ This cuts out all values of arg from a strinf """
    register.filter("cut", cut)
    return value.replace(arg, "")

