from django.shortcuts import render
def home(request):
   dados = {
      "nome": "Cadastro de cursos Cyber Dev"
   }
   return render (request,"curso_app/home.html", dados)

