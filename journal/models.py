from django.db import models
from django.utils import timezone

class Paper(models.Model):
    AREA_CHOICES = [
        ('engineering', 'Engineering'),
        ('science', 'Science'),
        ('technology', 'Technology'),
        ('medical', 'Medical'),
        ('management', 'Management'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    paper_file = models.FileField(upload_to='papers/')
    area_of_research = models.CharField(max_length=50, choices=AREA_CHOICES, default='engineering')
    author_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    prev_paper = models.CharField(max_length=200, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    
    # Future reference fields
    saved_for_future = models.BooleanField(default=False)
    reference_note = models.TextField(blank=True)
    saved_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author_name}"

    def save(self, *args, **kwargs):
        if self.saved_for_future and not self.saved_date:
            self.saved_date = timezone.now()
        super().save(*args, **kwargs)

class CoAuthor(models.Model):
    paper = models.ForeignKey(Paper, related_name='coauthors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ArchiveIssue(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    volume = models.IntegerField()
    issue = models.IntegerField()

    def __str__(self):
        return f"{self.month} {self.year} | Volume: {self.volume} | Issue: {self.issue}"

class ArchivePaper(models.Model):
    archive_issue = models.ForeignKey(ArchiveIssue, related_name='papers', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='archive_papers/')
    read_more_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class LatestUpdate(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
