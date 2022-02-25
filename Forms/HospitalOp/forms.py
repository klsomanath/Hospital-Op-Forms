from django import forms
from datetime import date
from HospitalOp.models import ModelForms
class FormName(forms.ModelForm):
    class Meta:
        model = ModelForms
        todays_date = date.today()
        YEARS = [x for x in range(1964,todays_date.year+1)]
        fields = ('Name','Age','Email','BP','gender1', 'YEARS1', 'WEIGHT1', 'PBFC1', 'DRFC1')
        widgets = {
            'gender1':forms.RadioSelect,
            'YEARS1':forms.SelectDateWidget(years=YEARS),
            'WEIGHT1':forms.Select,
            'PBFC1':forms.Select,
            'DRFC1':forms.Select
        }
