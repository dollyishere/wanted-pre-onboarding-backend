from django import forms
from recruitment_app.models import Company, User, Recruitment, Resume

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = []