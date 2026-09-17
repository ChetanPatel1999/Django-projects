from django.forms import ModelForm
from .models import UploadedFile
class UploadedFileForm(ModelForm):
    class Meta:
        model=UploadedFile
        fields='__all__' # make a form for all the fields of the model