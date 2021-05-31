from .serializers import ItemSerializer
from django.shortcuts import render
from rest_framework import generics, status
from .models import Items
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.


class ItemView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

class DeleteView(APIView):
  def delete(self, request, format=None):
     if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create() 
     Items.objects.all().delete()
     return Response(status=status.HTTP_200_OK)

class GetItemsView(APIView):
  serializer_class = ItemSerializer
  def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
    data = Items.objects.all()
    if(len(data) > 0):
      return Response(data, status=status.HTTP_200_OK)
    else:
       print("Database is empty")
       return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class CreateItemsView(APIView):
    serializer_class = ItemSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            item_id = serializer.data.get('item_id')
            master_category = serializer.data.get('master_category')
            Item = Items(item_id=item_id,master_category=master_category)
            Item.save()
            return Response(ItemSerializer(Item).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
