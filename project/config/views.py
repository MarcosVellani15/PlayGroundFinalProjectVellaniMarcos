from django.http import HttpResponse

def saludo_con_input(request):
    nombre = input("Dinos cual es tu nombre: ")
    return print(f"Hola, {nombre}")
