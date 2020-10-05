from django.db import models

# Create your models here.
class Release(models.Model):

    releaseDesc = models.CharField(max_length=6000)
    releaseLink = models.CharField(max_length=6000)
    releaseDate = models.DateTimeField('date_published')
    releaseTitle = models.CharField(max_length=500,default='noTitle')
    releaseArtist = models.CharField(max_length=500,default='noArtists')



    def __str__(self):
        return self.releaseDesc


