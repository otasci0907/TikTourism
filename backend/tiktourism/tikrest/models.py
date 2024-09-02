from django.db import models
    
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.CharField(max_length=200)
    time_spent = models.FloatField(default=0)
    proximity = models.FloatField()
    prox_mi = models.BooleanField()
    liked = models.BooleanField()
    clicked = models.BooleanField()

    def __str__(self):
        out = "Name: {}\nRating: {}\nImage Link: {}\nDistance: {}".format(self.name, self.rating, self.image, self.proximity)
        if (self.prox_mi):
            out += " miles"
        else:
            out += " steps"
        return out

