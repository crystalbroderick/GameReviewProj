from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    gametitle=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    releasedate=models.DateField()
    gamerating=models.CharField(max_length=25)
    genre=models.CharField(max_length=255)
    developer=models.CharField(max_length=255)
    players=models.CharField(max_length=255)
    summary=models.TextField()

    def __str__(self):
        return self.gametitle

    class Meta:
        db_table='game'
        verbose_name_plural='games'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    game=models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        verbose_name_plural='reviews'