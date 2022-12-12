from django.http import HttpResponse
import datetime

def saludo (request):

    return HttpResponse("Hola Amigos")

def damefecha (request):

    fecha_actual=datetime.datetime.now()

    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)