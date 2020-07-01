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
    title = models.CharField(max_length=50)



class Ticket:
    # seance_id =
    pass


class Hall:
    pass


class DateMovieRange:
    # movie =
    # data =
    pass


class Seance(models.Model):
    DateMovieRange = models.ForeignKey(DateMovieRange)
    # begin_t =
    # end_t =
    hall_id = models.ForeignKey(Hall)


class Purchase:
    pass
