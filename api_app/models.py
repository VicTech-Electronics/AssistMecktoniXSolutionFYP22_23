from rest_framework.serializers import ModelSerializer
from main_app.models import Detail

# Create your models here.
class DetailSerializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'