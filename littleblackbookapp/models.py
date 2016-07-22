from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    website = models.URLField()
    address = models.TextField()


    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Professional(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    website = models.URLField()
    STUDENT = "SL"
    JUNIOR = "JL"
    PROFESSIONAL = "PL"
    EXPERT = "EL"
    PROFESSIONAL_LEVEL = (
        (STUDENT, "Student"),
        (JUNIOR, "Junior/Entry Level Professional"),
        (PROFESSIONAL, "Mid-Level Professional"),
        (EXPERT, "Expert"),
    )
    level = models.CharField(
        max_length=2,
        choices=PROFESSIONAL_LEVEL,
        default=PROFESSIONAL,
    )
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
    goals = models.TextField()
    address = models.TextField()
    email2 = models.EmailField()
    phone2 = models.CharField(max_length=12)
    website2 = models.URLField()
    company = models.ManyToManyField(Company)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
