from django.shortcuts import render
from .forms import CandidateForm
from django.shortcuts import redirect
# Create your views here.

def submit_form(request):
    return render(request,'form/submit_form.html',{})

def new_submition(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save()
            candidate.save()
            return redirect('../')
    else:
        form = CandidateForm()
    return render(request, 'submit/new_submition.html',{'form':form})
