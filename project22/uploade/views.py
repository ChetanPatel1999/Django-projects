from django.shortcuts import render,redirect
from .forms import UploadedFileForm
from .models import UploadedFile

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_files')
    else:
        form = UploadedFileForm()
    return render(request, 'uploade/image_upload.html', {'form': form})

def display_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'uploade/image_display.html', {'files': files})
