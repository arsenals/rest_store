from rest_framework import serializers

from .models import Product


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     description = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    #
    # def get_image(self, obj):
    #     image_obj = obj.images.first()
    #     if image_obj is not None and image_obj.image:
    #         return image_obj.image.url
    #     return ''

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price')

    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation
