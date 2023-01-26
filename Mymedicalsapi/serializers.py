from Mymedicals.models import medicine
from rest_framework import serializers

class medicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields = "__all__"