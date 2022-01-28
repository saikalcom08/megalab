from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name

class Organization(models.Model):
    org_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.org_name

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=50)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.country

class BankAccount(models.Model):
    account_number = models.CharField(max_length=16)
    created_date = models.DateTimeField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number

class Measurement(models.Model):
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    ratio = models.FloatField()

    def __str__(self):
        return self.full_name

class Good(models.Model):
    name_varchar = models.CharField(max_length=200)
    shipment_date = models.DateTimeField()
    measurement = models.ForeignKey('Measurement', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_varchar

class Operation(models.Model):
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField()
    sold_date = models.DateTimeField()
    good = models.ForeignKey('Good', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.price}'

class GoodsInOrganization(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    good = models.ForeignKey('Good', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.organization} -> {self.good}'