from django.shortcuts import render
from .forms import CandidateForm
# Create your views here.

def submit_form(request):
    return render(request,'form/submit_form.html',{})

def new_submition(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.first_name = request.user
            candidate.last_name = request.user
            candidate.school = request.user
            candidate.year = request.user
            candidate.text = request.user
            candidate.impact = request.user
            candidate.github = request.user
            candidate.email = request.user
            candidate.save()
            return redirect('submit_form', pk=post.pk)
    else:
        form = CandidateForm()
    return render(request, 'submit/new_submition.html',{'form':form})
