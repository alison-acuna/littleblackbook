from django.db import models
from django.utils import timezone

# Implemented for stream_framework
from stream_framework.feeds.redis import RedisFeed
from stream_framework.feed_managers.base import Manager

# Create your models here.

class Strengths(models.Model):
    strengths = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

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
    strengths = models.ManyToManyField(Strengths)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField()
    professional = models.ForeignKey(
    'Professional',
    on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

# Social Media

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Implemented for stream_framework

# class PinFeed(RedisFeed):
#     key_format = 'feed:normal:%(user_id)s'
#
# class UserPinFeed(PinFeed):
#     key_format = 'feed:user:%(user_id)s'
#
# class PinManager(Manager):
#     feed_classes = dict(
#         normal=PinFeed,
#     )
#     user_feed_class = UserPinFeed
#
#     def add_pin(self, pin):
#         activity = pin.create_activity()
#         # add user activity adds it to the user feed, and starts the fanout
#         self.add_user_activity(pin.user_id, activity)
#
#     def get_user_follower_ids(self, user_id):
#         ids = Follow.objects.filter(target=user_id).values_list('user_id', flat=True)
#         return {FanoutPriority.HIGH:ids}
#
# manager = PinManager()

# implement your feed with redis as storage
