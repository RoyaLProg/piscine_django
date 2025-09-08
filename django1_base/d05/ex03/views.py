from django.shortcuts import render


def index(request):
    return render(request, "ex03/index.html", {"range": [int(i * 255/50) for i in range(50)]})
