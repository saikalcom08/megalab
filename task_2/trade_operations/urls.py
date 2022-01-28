from django.urls import path
from trade_operations.views import OwnerListAPIView, OwnerCreateAPIView, OwnerUpdateAPIView, \
    OrganizationListAPIView, OrganizationCreateAPIView, OrganizationUpdateAPIView, \
    AddressListAPIView, AddressCreateAPIView, AddressUpdateAPIView, \
    BankAccountListAPIView, BankAccountCreateAPIView, BankAccountUpdateAPIView, \
    MeasurementListAPIView, MeasurementCreateAPIView, MeasurementUpdateAPIView, \
    GoodListAPIView, GoodCreateAPIView, GoodUpdateAPIView, \
    OperationListAPIView, OperationCreateAPIView, OperationUpdateAPIView

urlpatterns = [
    path('owner/', OwnerListAPIView.as_view()),
    path('owner-create/', OwnerCreateAPIView.as_view()),
    path('owner-update/<int:pk>/', OwnerUpdateAPIView.as_view()),
    path('organization/', OrganizationListAPIView.as_view()),
    path('organization-create/', OrganizationCreateAPIView.as_view()),
    path('organization-update/<int:pk>/', OrganizationUpdateAPIView.as_view()),
    path('address/', AddressListAPIView.as_view()),
    path('address-create/', AddressCreateAPIView.as_view()),
    path('address-update/<int:pk>/', AddressUpdateAPIView.as_view()),
    path('bankAccount/', BankAccountListAPIView.as_view()),
    path('bankAccount-create/', BankAccountCreateAPIView.as_view()),
    path('bankAccount-update/<int:pk>/', BankAccountUpdateAPIView.as_view()),
    path('measurement/', MeasurementListAPIView.as_view()),
    path('measurement-create/', MeasurementCreateAPIView.as_view()),
    path('measurement-update/<int:pk>/', MeasurementUpdateAPIView.as_view()),
    path('good/', GoodListAPIView.as_view()),
    path('good-create/', GoodCreateAPIView.as_view()),
    path('good-update/<int:pk>/', GoodUpdateAPIView.as_view()),
    path('operation/', OperationListAPIView.as_view()),
    path('operation-create/', OperationCreateAPIView.as_view()),
    path('operation-update/<int:pk>/', OperationUpdateAPIView.as_view()),
]