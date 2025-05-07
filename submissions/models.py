from django.db import models

# Create your models here.
from django.db import models

class StartupSubmission(models.Model):
    founder_name = models.CharField(max_length=100)
    startup_name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField()
    pitch_deck = models.FileField(upload_to='pitch_decks/')
    submitted_at = models.DateTimeField(auto_now_add=True)
