from InventoryEngineApp.models import *
from InventoryEngineApp.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class ValidateInventoryApiView(APIView):
        def get_object(self, pk):
            try:
                return Inventory.objects.get(itemCode=pk)
            except Inventory.DoesNotExist:
                return None


        def get(self, request, itemCode, requestNumber, format=None):
            inventory = self.get_object(itemCode)
            #Check if requested quantity is available 
            if inventory == None:
                return JsonResponse('NotAvailable', safe=False) 
            #Check if requested quantity is available 
            if inventory.quantity < requestNumber:
                return JsonResponse('NotAvailable', safe=False) 
                
            inventory.quantity = inventory.quantity - requestNumber
            inventory.save()
            
            return JsonResponse('Available', safe=False)

class CreateInventoryApiView(APIView):
            """
            Inventory List and post
            """
            def post(self, request, format=None):
                    serializer = InventorySerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def get(self, request, format=None):
                    inventory = Inventory.objects.all()
                    serializer = InventorySerializer(inventory, many=True)
                    return Response(serializer.data)


class InventoryApiView(APIView):
        """
        Retrieve, update or delete a snippet instance.
        """
        def get_object(self, pk):
            try:
                return Inventory.objects.get(pk=pk)
            except Inventory.DoesNotExist:
                raise Http404



        def put(self, request, pk, format=None):
            inventory = self.get_object(pk)
            serializer = InventorySerializer(inventory, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        

 

