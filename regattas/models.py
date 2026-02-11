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
        
class Race(models.Model):
    #this result class will show the results of the regatta
    race_category = models.CharField(
        max_length=20,
        choices = [
        ('junior', 'U14'),
        ('senior', 'U16/Open'),
        ('masters', 'Masters'),
        ('lightweight', 'Lightweight'),
        ]
    )
    
    boat_class = models.CharField(
        max_length=20,
    choices = [
        ('single', 'Single'),
        ('pair', 'Pair'),
        ('four', 'Four'),
        ('double', 'Double'),
        ('quadruple', 'Quadruple'),
        ('octuple', 'Octuple'),
        ('eight', 'Eight'),
    ]
    )

    gender = models.CharField(max_length=6,
                              choices = [
                                  ('male', 'Male'),
                                  ('female', 'Female'),
                              ]
    )

    race_number = models.IntegerField()
    distance = models.IntegerField(blank=True, null=True)
    event_number = models.IntegerField()
    regatta = models.ForeignKey(Regatta, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.race_category} {self.race_number} {self.boat_class})"
    
class Result(models.Model):
    #this result class will show the results of the regatta
    race = models.ForeignKey(Race, related_name='results', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, related_name='club', on_delete=models.CASCADE)
    crew_names = models.CharField(max_length=200, blank=True)
    finish_time = models.CharField(max_length=20)
    finish_position = models.IntegerField()
    lane = models.IntegerField()


    def __str__ (self):
        return f"({self.race} {self.club} {self.crew_names} {self.finish_time} {self.lane})"

