def hipotenusa(catO, catA):
    return (catO**2 + catA**2) ** 0.5

def seno(catO, catA):
    hipo = hipotenusa(catO, catA)
    return catO / hipo

def cosseno(catO, catA):
    hipo = hipotenusa(catO, catA)
    return catA / hipo

def tangente(catO, catA):
    return seno(catO, catA)/cosseno(catO, catA)