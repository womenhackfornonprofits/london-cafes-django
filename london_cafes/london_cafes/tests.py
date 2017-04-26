from django.test import TestCase
from .models import Ratings, Cafe

class CafeManagerTestCase(TestCase):
	
	def setUp(self):
		rating3 = Ratings.objects.create(id=1, rating=3)
		rating5 = Ratings.objects.create(id=2, rating=5)
		rating1 = Ratings.objects.create(id=3, rating=1)
		Cafe.objects.create(id=1, name="cafe1", description="desc1", address1="a1", address2="a2", address3="a3", city="city1", post_code="A1 ABC", atmosphere_rating=rating5, coffee_rating=rating3, wifi_rating=rating3)
		Cafe.objects.create(id=2, name="cafe2", description="desc2", address1="a12", address2="a2", address3="a3", city="city1", post_code="A1 ABC", atmosphere_rating=rating5, coffee_rating=rating3, wifi_rating=rating1)
		Cafe.objects.create(id=3, name="cafe3", description="desc3", address1="a13", address2="a2", address3="a3", city="city1", post_code="A1 ABC", atmosphere_rating=rating1, coffee_rating=rating1, wifi_rating=rating1)

	def test_atmosphere_exact_ratings_filter(self):
		cafes_expected = Cafe.objects.filter(id__in=[1,2])
		cafes = Cafe.objects.atmosphere_exact_rating(5)
		self.assertItemsEqual(cafes, cafes_expected) 

	def test_coffee_exact_ratings_filter(self):
		cafes_expected = Cafe.objects.filter(id__in=[1,2])
		cafes = Cafe.objects.coffee_exact_rating(3)
		self.assertItemsEqual(cafes, cafes_expected)

	def test_wifi_exact_ratings_filter(self):
		cafes_expected = Cafe.objects.filter(id__in=[2,3])
		cafes = Cafe.objects.wifi_exact_rating(1)
		self.assertItemsEqual(cafes, cafes_expected)

	def test_atmosphere_gte_ratings_filter(self):
		cafes_expected = Cafe.objects.filter(id__in=[1,2])
		cafes = Cafe.objects.atmosphere_gte_rating(5)
		self.assertItemsEqual(cafes, cafes_expected)	    

	def test_coffee_gte_ratings_filter(self):
		cafes_expected = Cafe.objects.filter(id__in=[1,2])
		cafes = Cafe.objects.coffee_gte_rating(3)
		self.assertItemsEqual(cafes, cafes_expected)	

	def test_wifi_gte_ratings_filter(self):
		cafes_expected = Cafe.objects.filter(id__in=[1])
		cafes = Cafe.objects.wifi_gte_rating(2)
		self.assertItemsEqual(cafes, cafes_expected)			