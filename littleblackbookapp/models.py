from django.db import models

# Create your models here.

class Professional(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    website = models.URLField()
    DOWNTOWN = "DT"
    SOUTHEAST = "SE"
    REMOTE = "RR"
    WESTSIDE = "WS"
    NORTH = "NP"
    CLACKAMAS = "CK"
    NEIGHBORHOOD_CHOICES = (
        (DOWNTOWN, 'Downtown'),
        (SOUTHEAST, 'Southeast'),
        (REMOTE, 'Outside of Portland'),
        (WESTSIDE, 'Westside'),
        (NORTH, 'North Portland'),
        (CLACKAMAS, 'Clackamas'),
    )
    neighborhood = models.CharField(
        max_length=2,
        choices=NEIGHBORHOOD_CHOICES,
        default=DOWNTOWN,
    )


    def publish(self):
        self.save()

    def __str__(self):
        return self.name
