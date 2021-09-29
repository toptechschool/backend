from rest_framework import serializers
from api.models.note import Note
from users.models import User,Profile
from .taggit import TagListSerializerField
from users.serializers import ProfileSerializer


class NoteDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='note-detail-update',lookup_field='slug')
    date_posted = serializers.DateTimeField(format="%Y-%m-%d")
    date_updated = serializers.DateTimeField(format="%Y-%m-%d")
    author = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='get_liked_count')
    
    class Meta:
        model = Note
        fields = '__all__'

    def get_author(self,obj):
        profile = Profile.objects.get(user=obj.author)
        isAuthor = self.context['request'].user == obj.author
        return { 
            "name":profile.name,
            "avatar":self.context['request'].build_absolute_uri(profile.profile_pic.url),
            "bio":profile.bio,
            "username":obj.author.username,
            "isAuthor":isAuthor
        }


class NoteCreateSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Note
        fields = ['author','title','content','slug','tags']
        read_only_fields = ['author','slug']
        validators = []


class NoteListSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name='note-detail-update',lookup_field='slug')
    author = serializers.SerializerMethodField()
    date_posted = serializers.DateTimeField(format="%Y-%m-%d")
    date_updated = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Note
        fields = [
            'id',
            'author',
            'title',
            'date_posted',
            'date_updated',
            'slug',
            'views',
            'read_time',
            'get_liked_count',
            'tags',
            'url',
        ]
    def get_author(self,obj):
        profile = Profile.objects.get(user=obj.author)
        return {"name":profile.name,"username":obj.author.username}


class NoteListUserSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name='note-detail-update',lookup_field='slug')
    
    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'slug',
            'tags',
            'url',
        ]