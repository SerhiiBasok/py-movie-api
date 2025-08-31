from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
        ]

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "title",
            instance.title
        )
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.save()
        return instance

    def get_title(self, obj):
        return obj.title

    def get_description(self, obj):
        return obj.description
