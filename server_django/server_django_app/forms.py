from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class EmployeeFormStep1(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'middle_name', 'unit', 'position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'] = True
        self.fields['first_name'] = True
        self.fields['unit'].required = True
        self.fields['position'].required = True


class EmployeeFormStep2(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ('username')
        # Поля Password1 и Password2 добавятся автоматически
