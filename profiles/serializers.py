from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from products.models import Product
User = get_user_model()


class UserList(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields= [
            "url",
            "password",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "email",
            "is_author",
        ]
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None        
        return reverse("user-detail", kwargs={'pk':obj.pk}, request=request)

class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude= [
            'password',
            'user_permissions',
            'is_author',
            'groups'
            
        ]