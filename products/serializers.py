from .models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse


class ProductSerializers(serializers.ModelSerializer):
    url= serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'url',
            'username',
            'title',
            'description',
            'price',
            'active',
            ]
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None        
        return reverse("detail-delete-view", kwargs={'pk':obj.pk}, request=request)
    
    def get_username(self, obj):
        return obj.get_username