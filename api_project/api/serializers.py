from rest_framework import serializers
from .models import MyModel
serializers.ModelSerializer
class BookSerializer :
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at']