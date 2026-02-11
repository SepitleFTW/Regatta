from django.db import models

class Club(models.Model):
    #club class with blank=True for optional fields
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='club_logos/', blank=True, null=True)
    abbreviation = models.CharField(max_length=5, blank=True)
    website=models.URLField(blank=True)

    def __str__(self):
        #only return the name of the club, tuples not supported
        return f"({self.name} {self.abbreviation})"