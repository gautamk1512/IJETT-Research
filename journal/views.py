from django.shortcuts import render, redirect
from .models import Paper, CoAuthor, ArchiveIssue, ArchivePaper, LatestUpdate
from django import forms
from django.contrib import messages
from django.db import models

# Create your views here.

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = [
            'title', 'paper_file', 'area_of_research', 'author_name', 'institution', 'email', 'mobile',
            'address_line1', 'address_line2', 'country', 'state', 'city', 'pincode', 'prev_paper'
        ]

def home(request):
    updates = LatestUpdate.objects.order_by('-created_at')
    return render(request, 'journal/home.html', {'updates': updates})

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
    # Fetch all archive issues, newest first
    issues = ArchiveIssue.objects.order_by('-year', '-volume', '-issue')
    archive_issues = []
    query = request.GET.get('q', '').strip()
    for issue in issues:
        papers = issue.papers.all()
        if query:
            papers = papers.filter(
                models.Q(title__icontains=query) |
                models.Q(authors__icontains=query) |
                models.Q(id__icontains=query)
            )
        archive_issues.append({
            'month': issue.month,
            'year': issue.year,
            'volume': issue.volume,
            'issue': issue.issue,
            'papers': [
                {
                    'title': paper.title,
                    'authors': paper.authors,
                    'read_more_url': paper.read_more_url or '#',
                    'pdf_url': paper.pdf.url if paper.pdf else '#',
                }
                for paper in papers
            ]
        })
    return render(request, 'journal/archive.html', {'archive_issues': archive_issues, 'query': query})

def author_login(request):
    if request.method == 'POST':
        paper_id = request.POST.get('paper_id')
        email = request.POST.get('email')
        try:
            paper = Paper.objects.get(id=paper_id, email=email)
            request.session['author_paper_id'] = paper.id
            return redirect('authors')
        except Paper.DoesNotExist:
            messages.error(request, 'Invalid Paper ID or Email')
    return render(request, 'author_login.html')

def author_logout(request):
    if 'author_paper_id' in request.session:
        del request.session['author_paper_id']
    return redirect('author_login')

def authors(request):
    paper_id = request.session.get('author_paper_id')
    papers = Paper.objects.filter(id=paper_id) if paper_id else []
    return render(request, 'journal/authors.html', {'papers': papers})

def author_register(request):
    if request.method == 'POST':
        # Here you would add registration logic
        messages.success(request, 'Registration successful! You can now log in.')
    return render(request, 'author_register.html')

def call_for_paper(request):
    return render(request, 'call_for_paper.html')

def track_paper(request):
    paper = None
    status = None
    error = None
    if request.method == 'POST':
        paper_id = request.POST.get('paper_id')
        email = request.POST.get('email')
        try:
            paper = Paper.objects.get(id=paper_id, email=email)
            status = paper.get_status_display()
        except Paper.DoesNotExist:
            error = "Paper not found. Please check your Paper ID and Email."
    return render(request, 'journal/track_paper.html', {'paper': paper, 'status': status, 'error': error})
