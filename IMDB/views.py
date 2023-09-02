from rest_framework import viewsets
from .models import Filme, Pessoa
from .serializers import FilmeSerializer, PessoaSerializer

class FilmeViewset(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class PessoaViewset(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


        