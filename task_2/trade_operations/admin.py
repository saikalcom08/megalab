from django.contrib import admin
from .models import Owner, Organization, Address, BankAccount, Measurement, Good, Operation, GoodsInOrganization

admin.site.register(Owner)
admin.site.register(Organization)
admin.site.register(Address)
admin.site.register(BankAccount)
admin.site.register(Measurement)
admin.site.register(Good)
admin.site.register(Operation)
admin.site.register(GoodsInOrganization)

