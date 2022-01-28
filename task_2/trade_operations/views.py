# from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import OwnerSerializer, OrganizationSerializer, AddressSerializer, BankAccountSerializer, \
    MeasurementSerializer, GoodSerializer, OperationSerializer
from .models import Owner, Organization, Address, BankAccount, Measurement, Good, Operation

#owner
class OwnerListAPIView(ListAPIView):
    queryset = Owner.objects.all().order_by('first_name')
    serializer_class = OwnerSerializer

class OwnerCreateAPIView(CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

#organization
class OrganizationListAPIView(ListAPIView):
    queryset = Organization.objects.all().order_by('org_name')
    serializer_class = OrganizationSerializer

class OrganizationCreateAPIView(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

#address
class AddressListAPIView(ListAPIView):
    queryset = Address.objects.all().order_by('country')
    serializer_class = AddressSerializer

class AddressCreateAPIView(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class =AddressSerializer

class AddressUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

#bankAccount
class BankAccountListAPIView(ListAPIView):
    queryset = BankAccount.objects.all().order_by('account_number')
    serializer_class = BankAccountSerializer

class BankAccountCreateAPIView(CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class =BankAccountSerializer

class BankAccountUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

#measurement
class MeasurementListAPIView(ListAPIView):
    queryset = Measurement.objects.all().order_by('full_name')
    serializer_class = MeasurementSerializer

class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class =MeasurementSerializer

class MeasurementUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

#good
class GoodListAPIView(ListAPIView):
    queryset = Good.objects.all().order_by('name_varchar')
    serializer_class = GoodSerializer

class GoodCreateAPIView(CreateAPIView):
    queryset = Good.objects.all()
    serializer_class =GoodSerializer

class GoodUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

#operation
class OperationListAPIView(ListAPIView):
    queryset = Operation.objects.all().order_by('price')
    serializer_class = OperationSerializer

class OperationCreateAPIView(CreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

class OperationUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer