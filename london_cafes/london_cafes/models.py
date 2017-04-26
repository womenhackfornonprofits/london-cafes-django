from django.db import models

#class CafeQuerySet(models.QuerySet):
class CafeManager(models.Manager):

    def atmosphere_exact_rating(self, rating):
        return self.filter(atmosphere_rating__rating=rating)

    def coffee_exact_rating(self, rating):
        return self.filter(coffee_rating__rating=rating)

    def wifi_exact_rating(self, rating):
        return self.filter(wifi_rating__rating=rating)

    def atmosphere_gte_rating(self, rating):
        return self.filter(atmosphere_rating__rating__gte=rating)

    def coffee_gte_rating(self, rating):
        return self.filter(coffee_rating__rating__gte=rating)

    def wifi_gte_rating(self, rating):
        return self.filter(wifi_rating__rating__gte=rating)

RATING_OPTIONS = (
    (1, 'Not Good'),
    (2, 'OK'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'),
)

class Ratings(models.Model):
    rating = models.CharField(
        max_length=30,
        choices=RATING_OPTIONS,
        default=5)

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    description = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=30)
    atmosphere_rating = models.ForeignKey(Ratings, related_name="atmosphere_rating")
    coffee_rating = models.ForeignKey(Ratings, related_name="coffee_rating")
    wifi_rating = models.ForeignKey(Ratings, related_name="wifi_rating")

    objects = CafeManager()
