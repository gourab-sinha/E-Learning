from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, HyperlinkedRelatedField
from ..models import Subject, Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):


    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='courses:api-modules-detail',
        lookup_field='id',
    )
    class Meta:
        model = Module
        fields = ['url', 'order', 'description']


class CourseSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='courses:api-courses-detail',
        lookup_field='id',
    )

    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['url', 'id', 'subject', 'title', 'slug', 'overview',
                  'created', 'owner', 'modules']


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):

    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentsSerializer(serializers.ModelSerializer):

    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']


class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'slug',
                  'overview', 'created', 'owner', 'modules']
