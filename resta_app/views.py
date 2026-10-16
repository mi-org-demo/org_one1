from django.shortcuts import render
from django.http import JsonResponse
from scripts.calculadora import sumar, restar

import django
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'django_version': django.get_version()})


def api_calcular(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    try:
        a = request.POST.get('num1', '0')
        b = request.POST.get('num2', '0')
        op = request.POST.get('operacion', 'suma')
        fn = sumar if op == 'suma' else restar
        data = fn(a, b)
        data['operacion_tipo'] = op
        return JsonResponse(data)
    except (ValueError, TypeError) as e:
        return JsonResponse({'error': f'Números inválidos: {e}'}, status=400)