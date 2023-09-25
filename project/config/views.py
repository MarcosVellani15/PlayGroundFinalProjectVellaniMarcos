from django.http import HttpResponse

def saludo(request):
    nombre = input("Hola, dime tu nombre: ")
    return HttpResponse(f"Hola, {nombre.upper()}")

def numero_aleatorio(request):
    import random
    numero = random.randint(1,6)
    return HttpResponse(f"has tirado el dado {numero}")
