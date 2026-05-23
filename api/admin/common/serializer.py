from rest_framework import serializers
from apps.common.models import Phone, PhoneImage



class PhoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneImage
        fields = ['id', 'image']

class PhoneSerializer(serializers.ModelSerializer):
    images = PhoneImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)

    class Meta:
        model = Phone
        fields = ['id', 'title', 'created_at', 'images', 'uploaded_images']

    def create(self, validated_data):
        images = validated_data.pop('uploaded_images',[])
        phone = Phone.objects.create(**validated_data)
        for image in images:
            PhoneImage.objects.create(phone=phone, image=image)
        return phone