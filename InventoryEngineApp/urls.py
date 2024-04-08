from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from InventoryEngineApp.views import *

urlpatterns = [
    path('inventory/', CreateInventoryApiView.as_view()),
    path('inventory/<str:itemCode>/<int:requestNumber>/', ValidateInventoryApiView.as_view()),
    path('inventory/<int:pk>/', InventoryApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)