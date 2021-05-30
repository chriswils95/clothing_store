from rest_framework import serializers
from .models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'item_id', 'gender', 'master_category',
                  'sub_category', 'article_type', 'base_color',
                  'season', 'year', 'usage', 'display_name', 'image_path')
