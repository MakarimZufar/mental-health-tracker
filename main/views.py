from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306241751',
        'name': 'Makarim Zufar Prambudyo',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)