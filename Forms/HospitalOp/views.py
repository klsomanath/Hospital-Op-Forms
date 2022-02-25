from django.shortcuts import render
from . import forms
import csv
from django.http import HttpResponse
from HospitalOp.models import ModelForms
# Create your views here.
def index(request):
    return render(request,'index.html')
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = forms.FormName()
        else:
            print('From Invalid')
    return render(request,'form_page.html',{'form':form})
def forms_csvs(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Deposition'] = 'attachement; filename=forms.csv'
    writer =csv.writer(response)
    forms1 = ModelForms.objects.all()
    writer.writerow(['Name','Age','Email','Blood Pressure','Gender','Date of Birth','Weight','Problems Facing','Doctor Reffered'])
    for form2 in forms1:
        writer.writerow([form2.Name,form2.Age,form2.Email,form2.BP,form2.gender1,form2.YEARS1,form2.WEIGHT1,form2.PBFC1,form2.DRFC1])
    #return render(request,'form_csv.html',{'response':response})
    return response
def export_csv(request):
    return render(request,'form_csv.html')

