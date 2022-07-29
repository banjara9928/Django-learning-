from django.shortcuts import HttpResponse

# def index(request):
#     return HttpResponse('<h1>Hello Rohit</h1>')

    # fname = request.GET['fname']
    # lname = request.GET['lname']
    # return HttpResponse(f'<h1>Hello {fname} {lname}</h1>')
def add(request):
    power = request.GET['number']
    power = int(power)**2
    print(power)
    return HttpResponse(f'{power}' )
    # return HttpResponse(2 + 1 )