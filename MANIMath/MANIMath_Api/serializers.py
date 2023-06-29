from rest_framework import serializers
from MANIMath_Data.models import *

class FunctionModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    topic = serializers.CharField(source='topic.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = FunctionModel
        fields = '__all__'

class RootFindingModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    topic = serializers.CharField(source='topic.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = RootFindingModel
        fields = '__all__'

class SortModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    topic = serializers.CharField(source='topic.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = SortModel
        fields = '__all__'

class SearchModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    topic = serializers.CharField(source='topic.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = SearchModel
        fields = '__all__'
