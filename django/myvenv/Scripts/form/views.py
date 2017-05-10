from django.shortcuts import render
# Create your views here.

def submit_form(request):
    return render(request,'form/submit_form.html',{})
