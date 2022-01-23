from django.urls import path
from api.views.company import CompanyListCreateAPIView,CompanyRetrieveUpdateDestroyAPIView,CompanyLikeToggleAPIView
from api.views.job import JobListCreateAPIView,JobRetrieveUpdateDestroyAPIView,JobLikeToggleAPIView
from api.views.ranking import (
    QuestionListCreateAPIView,
    QuestionRetrieveUpdateDestroyAPIView,
    QuizRetrieveUpdateDestroyAPIView,
    QuizListCreateAPIView,
)

urlpatterns = [
    path('company/<str:slug>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-detail-update'),
    path('company/<int:company_id>/like-toggle/', CompanyLikeToggleAPIView.as_view(), name='company-like-toggle'),
    path('company/', CompanyListCreateAPIView.as_view(), name='company-list-create'),

    path('job/<int:job_id>/', JobRetrieveUpdateDestroyAPIView.as_view(), name='job-detail-update'),
    path('job/<int:job_id>/like-toggle/', JobLikeToggleAPIView.as_view(), name='job-like-toggle'),
    path('job/', JobListCreateAPIView.as_view(), name='job-list-create'),

    path('question/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('question/<int:id>/', QuestionRetrieveUpdateDestroyAPIView.as_view(), name='question-detail-update'),
    path('quiz/<str:slug>/', QuizRetrieveUpdateDestroyAPIView.as_view(), name='quiz-detail-update'),
    path('quiz/', QuizListCreateAPIView.as_view(), name='quiz-list-create'),
]

'''

1. Get articles by username - article/user/<str:username>/
2. Article Like toggle - article/<int:article_id>/like-toggle/
3. Get article detail - article/<int:article_id>/
4. Update article - article/<int:article_id>/
5. Delete article - article/<int:article_id>/
6. Get article list - article/ 
7. Create article - article/

8. Company list - company/
9. Create a company - comapany/

'''