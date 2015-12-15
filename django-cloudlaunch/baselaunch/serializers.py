# from django.contrib.auth.models import User, Group
# from rest_framework import serializers

from baselaunch import models
from rest_framework_mongoengine.serializers import DocumentSerializer


class ApplicationSerializer(DocumentSerializer):
    class Meta:
        model = models.Application


# class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Application


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Category


# class InfrastructureSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Infrastructure
#         fields = ('url', 'name')


# class AWSEC2Serializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.AWSEC2
#         fields = InfrastructureSerializer.Meta.fields + ('region_name',)


# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Image
#         # fields = ('url', 'name', 'image_id', 'description')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
