def formatear_numero(n):
    return int(n) if float(n).is_integer() else n


def _operar(a, b, op):
    num1 = float(a)
    num2 = float(b)
    resultado = num1 + num2 if op == 'suma' else num1 - num2
    simbolo = '+' if op == 'suma' else '-'
    return {
        'num1': formatear_numero(num1),
        'num2': formatear_numero(num2),
        'resultado': formatear_numero(resultado),
        'operacion': f'{formatear_numero(num1)} {simbolo} {formatear_numero(num2)} = {formatear_numero(resultado)}',
    }


def sumar(a, b):
    return _operar(a, b, 'suma')


def restar(a, b):
    return _operar(a, b, 'resta')