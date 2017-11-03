from django.db import models


class Ornanization(models.Model):
	name = models.CharField(max_length=20)
	department = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	duty = models.CharField(max_length=20)
	cell_phone = models.IntegerField(max_length=11)
	plane_number = models.IntegerField(max_length=11)
