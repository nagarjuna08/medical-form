from django import forms 
from .models import Patient,DISEASE_CHOICES
from django.core.exceptions import ValidationError
import re

MAX_FILE_SIZE = 5 * 1024 * 1024
class PatientForm(forms.ModelForm):
    existing_diseases = forms.MultipleChoiceField(
        choices=DISEASE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Patient
        fields = ['name','age','email','phone','gender','document_proof','previous_report','existing_diseases','problem','address','city','emergency_contact','agreement']
        
        widgets = {'problem': forms.Textarea(attrs={'class': 'form-control','rows': 2}),
                   'address': forms.Textarea(attrs={'class': 'form-control','rows': 2})}
    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = name.strip()
        if not name :
            raise ValidationError("Enter your name")
        if not re.fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", name):
            raise ValidationError("Name should contain only letters")
        return name
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise ValidationError("Phone must contain only digits")

        if len(phone) != 10:
            raise ValidationError("Phone must be exactly 10 digits")

        return phone
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise ValidationError("Enter age")
        if age <1  or age > 120:
            raise ValidationError("Age must be between 1 and 120")

        return age
    

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')

        if gender not in ['Male', 'Female']:
            raise ValidationError("Please select a valid gender")

        return gender
    
    def clean_document_proof(self):
        file = self.cleaned_data.get('document_proof')

        if not file:
            raise ValidationError("Document proof is required")

        if not file.name.endswith('.pdf'):
            raise ValidationError("Only PDF files are allowed")

        if file.size > MAX_FILE_SIZE:
            raise ValidationError("File size must be less than 2MB")

        return file 
    

    def clean_previous_report(self):
        file = self.cleaned_data.get('previous_report')

        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError("Only PDF allowed")

            if file.size > MAX_FILE_SIZE:
                raise ValidationError("File size must be less than 2MB")

        return file
    
    def clean_address(self):
        address = self.cleaned_data.get('address')

        if len(address.strip()) < 10:
            raise ValidationError("Address must be at least 10 characters")

        return address


    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city:
            raise ValidationError("Enter city")
        if not city.isalpha():
            raise ValidationError("City must contain only letters")

        return city


    def clean_emergency_contact(self):
        contact = self.cleaned_data.get('emergency_contact')

        if contact:
            if not contact.isdigit() or len(contact) != 10:
                raise ValidationError("Emergency contact must be 10 digits")

        return contact

    def clean_agreement(self):
        agreement = self.cleaned_data.get('agreement')

        if not agreement:
            raise ValidationError("You must accept the agreement")

        return agreement
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required")
        pattern= r'[A-Za-z0-9]+@[\w]+\.[\w]+'
        if not re.match(pattern, email):
            raise ValidationError("Only Gmail addresses are allowed")

        return email
    
    # def clean_existing_diseases(self):
    #     diseases = self.cleaned_data.get('existing_diseases')

    #     if diseases:
    #         return ', '.join(diseases)  

    #     return diseases
