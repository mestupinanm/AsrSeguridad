from ..models import Tipo

def get_tipos():
    queryset = Tipo.objects.all()
    return (queryset)

def create_tipo(form):
    tipo = form.save()
    tipo.save()
    return ()