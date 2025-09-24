from django.shortcuts import render

from decimal import Decimal, InvalidOperation
from django.shortcuts import render

def calculator(request):
    result = None
    error = None
    num1 = request.POST.get('num1', '')
    num2 = request.POST.get('num2', '')
    op = request.POST.get('operation', '')
    if request.method == 'POST':
        try:
            a = Decimal(num1)
            b = Decimal(num2)
            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            elif op == 'div':
                if b == 0:
                    error = 'Cannot divide by zero'
                else:
                    result = a / b
            else:
                error = 'Unknown operation'
        except InvalidOperation:
            error = 'Please enter valid numbers'
    return render(request, 'calculator/index.html', {
        'result': result,
        'error': error,
        'num1': num1,
        'num2': num2,
        'op': op,
    })

