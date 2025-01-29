from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    
    def num_of_ratings(self):
        ratings = Rating.objects.filter(movie=self) # select all rating in this database
        return len(ratings)
    
    def avg_of_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE) # if we remove the movie, we remove the rating
    user = models.ForeignKey(User, on_delete = models.CASCADE) # one to one # if we remove the user, we remove the rating
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('user','movie'),) # only accept the rating when (user,movie) is not in the database
        index_together = (('user','movie'),)