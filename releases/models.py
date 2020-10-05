from django.db import models

# Create your models here.
class Release(models.Model):

    releaseDesc = models.CharField(max_length=6000)
    releaseLink = models.CharField(max_length=6000)
    releaseDate = models.DateTimeField('date_published')

    def getallReleasesDesc(self):
        self.objects.all().order_by('-releaseDate')

    def getReleaseLinks(self):
        self.object.all()[0].releaseLink

    def __str__(self):
        return self.releaseDesc


