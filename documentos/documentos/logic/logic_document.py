from ..models import Document

def get_documents():
    queryset = Document.objects.all()
    return (queryset)

def create_documents(form):
    document = form.save()
    document.save()
    return ()