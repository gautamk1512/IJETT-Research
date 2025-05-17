from django.shortcuts import render, redirect
from .models import Paper, CoAuthor
from django import forms

# Create your views here.

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = [
            'title', 'paper_file', 'area_of_research', 'author_name', 'institution', 'email', 'mobile',
            'address_line1', 'address_line2', 'country', 'state', 'city', 'pincode', 'prev_paper'
        ]

def home(request):
    return render(request, 'journal/home.html')

def submit_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save()
            # Co-author handling will be added next
            return redirect('home')
    else:
        form = PaperForm()
    return render(request, 'journal/submit_paper.html', {'form': form})

def archive(request):
    papers = Paper.objects.order_by('-submitted_at')
    return render(request, 'journal/archive.html', {'papers': papers})
