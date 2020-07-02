from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class SimpleUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    wallet = models.DecimalField(max_digits=5, decimal_places=2)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Hall(models.Model):
    name = models.CharField(max_length=10)
    size = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.size}'


class DateMovieRange:
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True, blank=True)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)


class Seance(models.Model):
    name = models.CharField(max_length=200)
    DateMovieRange = models.ForeignKey(DateMovieRange, on_delete=models.CASCADE)
    begin_t = models.TimeField(null=True, blank=True)
    end_t = models.TimeField(null=True, blank=True)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_at', ]

    def __str__(self):
        return f'{self.name}'


class Ticket:
    seance_id = models.ForeignKey(Seance, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seance_id}'


class Purchase:
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
