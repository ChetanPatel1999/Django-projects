from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'age')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'border border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 w-full py-2 px-3',
                    'placeholder': 'Enter your name',
                    # 'value': 'John Doe',
                    }),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 w-full py-2 px-3'}),
            'age': forms.NumberInput(attrs={'class': 'border border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 w-full py-2 px-3'}),
        }
        labels = {
            'name': 'Student Name',
            'email': 'Email Address',
            'age': 'Student Age'
        }
        # help_texts = {
        #     'name': 'Please enter your full name.',
        #     'email': 'Please enter a valid email address.',
        #     'age': 'Please enter your age in years.'
        # }
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Age must be at least 18.")
        return age
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only letters and spaces.")
        return name