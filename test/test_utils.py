from src.utils import saludo, suma, es_par

def saludo_test():
    assert saludo("UIA") == "Hola UIA!"
    assert saludo("Conflicto") == "Hola Conflicto!"

def suma_test():
    assert suma(1, 2) == 3

def es_par_test():
    assert es_par(2) == True
    assert es_par(3) == False
