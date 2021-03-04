from django.db import models
from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = '__all__'
