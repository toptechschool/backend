from rest_framework import serializers
from api.models import Company


class CompanyDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail-update',lookup_field='slug')
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
        ]


class CompanyListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail-update',lookup_field='slug')
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