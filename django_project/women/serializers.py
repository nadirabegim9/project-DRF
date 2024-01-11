import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)


# def encode():
#     model = WomenModel('Гульнур Сатылганова', 'Content: Гульнур Сатылганова')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"\xd0\x93\xd1\x83\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x83\xd1\x80 \xd0\xa1\xd0\xb0\xd1\x82\xd1\x8b\xd0\xbb\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0","content":"Content: \xd0\x93\xd1\x83\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x83\xd1\x80 \xd0\xa1\xd0\xb0\xd1\x82\xd1\x8b\xd0\xbb\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)