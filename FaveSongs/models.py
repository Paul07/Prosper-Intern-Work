from django.db import models

# Create your models here.
TYPE_CHOICES = {
    ('Rock', 'Rock'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Classical', 'Classical'),
    ('Oldies', 'Oldies'),
    ('Disco', 'Disco'),
    ('Electronic', 'Electronic')
}

class FaveSongsModel(models.Model):
    Genre = models.CharField(max_length=50, choices=TYPE_CHOICES)
    Name = models.CharField(max_length=50, default="", blank=True, null=False)
    Artist = models.CharField(max_length=50, default="", blank=True, null=False)
    Album = models.CharField(max_length=50, default="", blank=True, null=False)
    Why = models.CharField(max_length=250, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Name
