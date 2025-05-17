from django.db import models

# Create your models here.

class Paper(models.Model):
    AREA_CHOICES = [
        ('cs', 'Computer Science'),
        ('ee', 'Electrical Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    paper_file = models.FileField(upload_to='papers/')
    area_of_research = models.CharField(max_length=50, choices=AREA_CHOICES, default='other')
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

    def __str__(self):
        return self.title

class CoAuthor(models.Model):
    paper = models.ForeignKey(Paper, related_name='coauthors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.name
