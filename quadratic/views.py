from django.shortcuts import render
from math import sqrt
from django.http import HttpResponse

# # Create your views here.
def quadratic_results(request):
    coefficients = {'a':'','b':'','c':''}
    description = {'a':'','b':'','c':''}
    d = False
    result = False
    solution = True
    for key,val in request.GET.items():
        val_desc = ''
        if val=='':
            val_desc = "Value was not provided"
            solution = False
        elif key=='a' and val=='0':
            val = 0
            val_desc = "Coefficient a cannot be 0"
            solution = False
        else:
            try:
                val = int(val)
            except:
                val_desc = "Incorrect value was provided"
                solution = False
        if key in coefficients.keys():
            coefficients[key] = val
            description[key] = val_desc


    if solution==True:
        a = coefficients['a']
        b = coefficients['b']
        c = coefficients['c']
        d = int(b*b -4*a*c)
        if d>0:
            result = [(-b+sqrt(d))/(2*a), (-b-sqrt(d))/(2*a)]
        elif d==0:
            result = -b/2*a

    return render(request, 'quadratic/results.html', {'coefficients':coefficients,
                                                      'result':result,
                                                      'discriminant':d,
                                                      'val_desc':description,
                                                      })