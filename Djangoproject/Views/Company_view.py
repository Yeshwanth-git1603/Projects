from django.shortcuts import render
from Myproject.models import Company
from Myproject.forms import CompanyForm
from django.http import HttpResponse
# Create your views here.

def CompanyView(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            ori=form.cleaned_data['origin']
            ce=form.cleaned_data['ceo']
            val=form.cleaned_data['valuation']
            ty=form.cleaned_data['type']
            c=Company(name=nm,origin=ori,ceo=ce,valuation=val,type=ty)
            c.save()

    else:
        form = CompanyForm()
    return render(request,"company.html",{'form':form})


