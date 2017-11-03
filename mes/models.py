from django.db import models


class PROJECT(models.Model):
	project_id = models.IntegerField(auto_created=True, primary_key=True)
	project_number = models.CharField(max_length=40)
	project_name = models.CharField(max_length=100)
	project_status = models.IntegerField(choices=(('01','排产阶段'), ('02','设计阶段'), ('03','组屏阶段'),))

