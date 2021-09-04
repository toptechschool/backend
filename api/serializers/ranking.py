from rest_framework import serializers
from api.models import Question, Option, Quiz


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
        read_only_fields = [
            'question',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'

    def create(self,validated_data):
        options_data = validated_data.pop('options')
        question = Question.objects.create(**validated_data)

        for option in options_data:
            Option.objects.create(question=question,**option)
        
        return question

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizRetrieveSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = [
            'slug',
            'id',
            'number_of_questions',
            'created_by',
        ]

class QuizListCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='quiz-detail-update',lookup_field='slug')
    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'slug',
            'number_of_questions',
            'url'
        ]
        read_only_fields = [
            'slug',
            'id',
            'number_of_questions'
        ]