from django.shortcuts import render
def home(request):
   dados = {
      "nome": "Sistema de cadastro"
   }
   return render (request,"curso_app/home.html", dados)

