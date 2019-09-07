from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    address = models.CharField(max_length=60, blank=True)
    town = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    events = models.ManyToManyField('Event', related_name='Actor', blank=True)
    volunteer = models.BooleanField()
    staff = models.BooleanField()
    donor = models.BooleanField()
    voter = models.BooleanField()
    journalist = models.BooleanField()
    precinct = models.ForeignKey(
        'Precinct',
        on_delete=models.CASCADE, blank=True, null=True
    )
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60, blank=True, null=True)
    town = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    when = models.DateField()
    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    reps = models.ManyToManyField('Actor', related_name='Media', blank=True, null=True)
    def __str__(self):
        return self.name

class Precinct(models.Model):
    number = models.CharField(max_length=30)
    town = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    def __str__(self):
        return self.number

class Contacts(models.Model):
    when = models.DateField()
    who_reached_out = models.CharField(max_length=60)
    target = models.ManyToManyField('Actor', related_name='Contacts')
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.target
