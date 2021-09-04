from rest_framework import serializers
from api.models import Company


class VideoLinkListField(serializers.ListField):
    def to_representation(self, data):
        return ','.join(data.values_list('link', flat=True))

class CompanyDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail-update',lookup_field='slug')
    get_video_links = VideoLinkListField(required=False)
    class Meta:
        model = Company
        fields = [
            'url',
            'name',
            'logo',
            'founded',
            'address',
            'description',
            'title',
            'website',
            'jobs',
            'facebook_link',
            'twitter_link',
            'linkedin_link',
            'get_video_links'
        ]


class CompanyListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail-update',lookup_field='slug')
    get_video_links = VideoLinkListField(required=False)
    class Meta:
        model = Company
        fields = [
            'url',
            'name',
            'logo',
            'founded',
            'address',
            'description',
            'title',
            'website',
            'jobs',
            'facebook_link',
            'twitter_link',
            'linkedin_link',
            'get_video_links'
        ]


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name',
            'logo',
            'founded',
            'address',
            'description',
            'title',
            'website',
            'jobs',
            'facebook_link',
            'twitter_link',
            'linkedin_link',
        ]