from django.db import models

class Paper(models.Model):
    AREA_CHOICES = [
        ('engineering', 'Engineering'),
        ('sci_tech', 'Science & Technology'),
        ('pharmacy', 'Pharmacy'),
        ('science', 'Science (Physics/Chemistry/Maths/Biology)'),
        ('commerce', 'Commerce'),
        ('economics', 'Economics'),
        ('management', 'Management'),
        ('hospitality', 'Hospitality and Tourism'),
        ('arts', 'Arts'),
        ('medical', 'Medical Science'),
        ('life_science', 'Life Sciences'),
        ('health_medical', 'Health & Medical Science'),
        ('social_science', 'Social Science and Humanities'),
        ('law', 'LAW & Education'),
        ('biotech', 'Biotechnology'),
    ]

    title = models.CharField(max_length=200)
    paper_file = models.FileField(upload_to='papers/')
    area_of_research = models.CharField(max_length=50, choices=AREA_CHOICES, default='engineering')
    author_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=200, default="N/A")
    address_line2 = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, default="N/A")
    state = models.CharField(max_length=100, default="N/A")
    city = models.CharField(max_length=100, default="N/A")
    pincode = models.CharField(max_length=20, default="000000")
    prev_paper = models.CharField(max_length=200, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return self.title

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
