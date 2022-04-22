from dataclasses import field
from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer()
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"
        # fields = ("title", "descripriton", "body")

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """Check that description and title are different"""
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and Description must be different!"
            )
        return data

    def validate_title(self, value):
        """Check that the title is at least 10 characters long"""
        if len(value) < 10:
            raise serializers.ValidationError(
                "The title has to be at least 10 characters"
            )
        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="article-detail"
    )
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateField(read_only=True)
#     updated_at = serializers.DateField(read_only=True)

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_date):
#         instance.author = validated_date.get("author", instance.author)
#         instance.title = validated_date.get("title", instance.title)
#         instance.description = validated_date.get(
#             "description", instance.description
#         )
#         instance.body = validated_date.get("body", instance.body)
#         instance.location = validated_date.get("location", instance.location)
#         instance.publication_date = validated_date.get(
#             "publication_date", instance.publication_date
#         )
#         instance.active = validated_date.get("active", instance.active)
#         instance.save()
#         return instance
