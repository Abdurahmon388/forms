from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.paginator import Paginator

from .models import UploadedFile
from threading import Thread


def index(request):
    return render(request, 'files/index.html')


def add_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        file_name = request.POST['name']
        file_path = default_storage.save(f'uploads/{uploaded_file.name}', uploaded_file)
        def save_file():
            UploadedFile.objects.create(file=file_path, name=file_name)
        thread = Thread(target=save_file)
        thread.start()
        return redirect('index')
    return render(request, 'files/add_file.html')


def search_file(request):
    search_query = request.GET.get('ok', '')
    files = UploadedFile.objects.filter(name__icontains=search_query).order_by('-uploaded_at')
    paginator = Paginator(files, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'files/search_file.html', {'page_obj': page_obj, 'search_query': search_query})
