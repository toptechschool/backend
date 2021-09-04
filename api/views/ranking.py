from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import filters, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.ranking import QuestionSerializer,QuestionListSerializer,QuizRetrieveSerializer,QuizListCreateSerializer
from api.models import Question,Quiz


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'


class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['question_genre']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuestionSerializer
        return QuestionListSerializer

#Quiz
class QuizRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuizRetrieveSerializer
    queryset = Quiz.objects.all()
    lookup_field = 'slug'


class QuizListCreateAPIView(ListCreateAPIView):
    serializer_class = QuizListCreateSerializer
    queryset = Quiz.objects.all()