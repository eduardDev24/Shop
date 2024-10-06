from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def electronica(request):
    data = {
        'titulo' : 'Electronica',
        'producto1' : 'Mac',
        'producto2' : 'Celular',
        'producto3' : 'Playstation'
    }
    return render(request, 'productos.html', data)

def juguetes(request):
    data = {
        'titulo' : 'Jugueytes',
        'producto1' : 'Pelota',
        'producto2' : 'Figura de acción',
        'producto3' : 'Juegos de mesa'
    }
    return render(request, 'productos.html', data)

def ropa(request):
    data = {
        'titulo' : 'Ropa',
        'producto1' : 'Polera',
        'producto2' : 'Chaqueta',
        'producto3' : 'Zapatilla'
    }
    return render(request, 'productos.html', data)