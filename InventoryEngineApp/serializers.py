from django.db.models import fields
from rest_framework import serializers
from InventoryEngineApp.models import *

class InventorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Inventory
		fields = ('itemCode', 'quantity')
