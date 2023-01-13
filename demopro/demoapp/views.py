from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
   obj=Place.objects.all()
   tng=Team.objects.all()
   return render(request,"index.html",{'result':obj,'res':tng})
# def register(request):
#    return render(request,"register.html")
# def home(request):
#     return HttpResponse("Welcome to Home Page")
# def details(request):
#     return HttpResponse("Welcome to Details Page")
# def about (request):
#     return HttpResponse("Welcome to About Page")
# def contact(request):
#     return HttpResponse("Welcome to Contact Page")
# def feedback(request):
#     return HttpResponse("Welcome to Feedback Page")