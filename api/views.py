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
     print("Another One")
     Items.objects.all().delete()
     print("ok One")
     return Response(status=status.HTTP_200_OK)


class CreateItemsView(APIView):
    serializer_class = ItemSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            item_id = serializer.data.get('item_id')
            gender = serializer.data.get('gender')
            master_category = serializer.data.get('master_category')
            sub_category = serializer.data.get('sub_category')
            article_type = serializer.data.get('article_type')
            base_color = serializer.data.get('base_color')
            season = serializer.data.get('season')
            year = serializer.data.get('year')
            usage = serializer.data.get('usage')
            display_name = serializer.data.get('display_name')
            image_path = serializer.data.get('image_path')
            Item = Items(item_id=item_id, gender=gender, master_category=master_category,
                         sub_category=sub_category, article_type=article_type, base_color=base_color,
                         season=season, year=year, usage=usage, display_name=display_name, image_path=image_path)
            Item.save()
            return Response(ItemSerializer(Item).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
