from django.shortcuts import render
from .forms import SimpleForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.conf import settings
from datetime import datetime


def index(request):
    if request.method == "GET":
        formated_history = []
        try:
            file = open(settings.HISTORY_LOG_FILE, 'r')
            history = [line for line in file.readlines()]
            file.close()

            for h in history:
                splitted = h.split('|')
                print(splitted)
                if len(splitted) == 2:
                    formated_history.append(
                            {"time": splitted[0], "text": splitted[1]})
        except:
            formated_history = []
        return render(request, "ex02/index.html",
                      {"form": SimpleForm(), "history": formated_history})

    elif request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            file = open(settings.HISTORY_LOG_FILE, 'a')
            file.write(f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}|{form.cleaned_data['textField']}\n")
            file.close()

            return HttpResponseRedirect("/ex02/")
        return HttpResponseBadRequest()
