# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Banks(models.Model):
	id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=49)

	class Meta:
		db_table = 'banks'

class Branches(models.Model):
	ifsc = models.CharField(max_length=11, null=False, primary_key=True)
	branch = models.CharField(max_length=74, null=True)
	address = models.CharField(max_length=195, null=True)
	city = models.CharField(max_length=50, null=True)
	district = models.CharField(max_length=50, null=True)
	state = models.CharField(max_length=26, null=True)
	bank = models.ForeignKey(Banks, null=True)

	class Meta:
		db_table = 'branches'