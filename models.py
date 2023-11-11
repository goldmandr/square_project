# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=60, blank=True, null=True)
    area = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    region = models.CharField(max_length=60, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    housenumber = models.CharField(max_length=60, blank=True, null=True)
    metro = models.CharField(max_length=60, blank=True, null=True)
    realestateid = models.ForeignKey('Realestate', models.DO_NOTHING, db_column='realestateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class DirectLink(models.Model):
    link = models.CharField(unique=True, max_length=250)
    realestateid = models.ForeignKey('Realestate', models.DO_NOTHING, db_column='realestateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directlink'


class Photo(models.Model):
    url = models.CharField(max_length=250)
    realestateid = models.ForeignKey('Realestate', models.DO_NOTHING, db_column='realestateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class Price(models.Model):
    price = models.TextField()  # This field type is a guess.
    area = models.IntegerField()
    realestateid = models.ForeignKey('Realestate', models.DO_NOTHING, db_column='realestateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'


class RealEstate(models.Model):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    description = models.TextField()
    pricepersquaremeter = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'realestate'


class RealEstateResource(models.Model):
    realestateid = models.ForeignKey(Realestate, models.DO_NOTHING, db_column='realestateid', blank=True, null=True)
    resourceid = models.ForeignKey('Resource', models.DO_NOTHING, db_column='resourceid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realestate_resource'


class Resource(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    link = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'resource'
