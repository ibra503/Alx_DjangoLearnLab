from rest_framework import serializers
from .models import MyModel

class BookSerializer :
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at']