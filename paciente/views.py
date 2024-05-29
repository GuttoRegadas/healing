from django.shortcuts import render

# Create your views here.
def home(resquest):
    if resquest.method == "GET":

        return render(resquest, 'home.html')