from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Potwierdzenie hasła")
    
    first_name = forms.CharField(max_length=50, label="Imię")
    last_name = forms.CharField(max_length=50, label="Nazwisko")
    phone = forms.CharField(max_length=20, label="Telefon")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data urodzenia")
    identity_document_type = forms.CharField(max_length=50, label="Typ dokumentu tożsamości")
    identity_document_no = forms.CharField(max_length=100, label="Numer dokumentu tożsamości")

    class Meta:
        model = User
        fields = ['username', 'email']  # Tylko te pola z modelu User
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'ala@makula.pl'}),
            'username': forms.TextInput(attrs={'placeholder': 'alamakota'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        
        if password != password_confirmation:
            raise forms.ValidationError("Hasła muszą być takie same!")
        
        return cleaned_data
