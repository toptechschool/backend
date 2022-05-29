from rest_framework import serializers
from api.models.blog import Blog
from users.models import Profile
from users.serializers import ProfileSerializer
from .taggit import TagListSerializerField


class BlogDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog-detail-update', lookup_field='slug')
    date_posted = serializers.DateTimeField(format="%Y-%m-%d")
    date_updated = serializers.DateTimeField(format="%Y-%m-%d")
    author = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='get_liked_count')
    
    class Meta:
        model = Blog
        fields = '__all__'

    def get_author(self,obj):
        profile = Profile.objects.get(user=obj.author)
        isAuthor = self.context['request'].user == obj.author
        return {"name":profile.name, "avatar": self.context['request'].build_absolute_uri(profile.profile_pic.url), "bio":profile.bio, "username":obj.author.username, "isAuthor":isAuthor}
    # def get_author(self,obj):
    #     profile = Profile.objects.get(user=obj.author)
    #     serializer = ProfileSerializer(profile).data
    #     return serializer

class BlogCreateSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'slug', 'tags']
        read_only_fields = ['author','slug']
        validators = []


class BlogListSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name='blog-detail-update',lookup_field='slug')
    author = serializers.SerializerMethodField()
    date_posted = serializers.DateTimeField(format="%Y-%m-%d")
    date_updated = serializers.DateTimeField(format="%Y-%m-%d")
    
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'date_posted', 'date_updated', 'slug', 'views', 'read_time', 'get_liked_count', 'tags', 'url',]
    
    def get_author(self,obj):
        profile = Profile.objects.get(user=obj.author)
        return {"name":profile.name, "username":obj.author.username}


class BlogListUserSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name='blog-detail-update', lookup_field='slug')
    
    class Meta:
        model = Blog
        fields = [ 'id', 'title', 'slug', 'tags', 'url', ]