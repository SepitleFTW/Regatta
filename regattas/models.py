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
    
class Regatta(models.Model):
    #this regatta class will show regatta locations and times
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='regatta_logos/', blank=True, null=True)
    venue = models.CharField(max_length=100)
    date= models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('upcoming', 'Upcoming'),
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
        ],
        default = 'upcoming'
    )
    description = models.TextField(blank=True)
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"({self.name} {self.date})"
        