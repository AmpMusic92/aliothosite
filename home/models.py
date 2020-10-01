from django.db import models

# Create your models here.
class MenuField (models.Model):
    menuField = models.CharField(max_length=200)

    def getRelatedLinkText(self):
        link = self.links_set.all()[0].link_text

        if len(link) != 0:
            return link
        else:
            raise Exception("Colonna senza link")

    def __str__(self):
        return self.menuField

class Links (models.Model):
    link = models.ForeignKey(MenuField,on_delete= models.CASCADE)
    link_text = models.CharField(max_length =1000)



    def __str__(self):
        return self.link_text


class Title (models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title