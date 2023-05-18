from rest_framework.serializers import ModelSerializer
from main_app.models import Due

# Create your models here.
class DueSerializer(ModelSerializer):
    class Meta:
        model = Due
        fields = ['customer', 'amount']