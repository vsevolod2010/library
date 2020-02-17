from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
import datetime


def max_date_validator(date):
    if date > datetime.datetime.now().date():
        raise ValidationError(
            _('%(value)s should be less %(now)s'),
            params={'value': date, 'now': datetime.datetime.now().date()},
        )


class Author(models.Model):

    name = models.CharField(max_length=50)
    birthday = models.DateField(validators=[max_date_validator])
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=50)
    annotation = models.CharField(max_length=1000)
    publication_year = models.IntegerField(validators=[MaxValueValidator(datetime.datetime.now().year)])
    authors = models.ManyToManyField(Author)

    def author_list(self):
        authors_list = self.authors.prefetch_related()
        authors = authors_list[0].name
        for i in range(1, authors_list.count()):
            authors += ', ' + authors_list[i].name
        return authors

    def __str__(self):
        return self.title
