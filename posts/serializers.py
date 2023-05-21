from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    # ModelSerializer class is a built in class to eliminate
    # defining id, title, content, author again in case it
    # is used with serializers.Serializer

    class Meta:
        model = Post
        field = ['id', 'title', 'content', 'author']

    # for below lines PostSerializer must inherit from serializers.Serializer
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    # content = serializers.CharField(style={'base_template': 'textarea.html'})
    # author = serializers.CharField(required=True, allow_blank=True, max_length=100)

    # how the instances will be created or updated when save is called
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance