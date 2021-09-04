from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import filters, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.job import JobSerializer
from api.views.paginations import JobPageNumberPagination
from api.models import Job
from api.models.choices import JOB_TYPE_CHOICES


class JobListCreateAPIView(ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    pagination_class = JobPageNumberPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['job_type']
    search_fields = ['location', 'title','description','responsibilities','technologies__name'] 


class JobRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'job_id'


class JobLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self,request,job_id):
        user = request.user
        job = get_object_or_404(Job,id=job_id)
        if job.favourite.filter(id=user.id).exists():
            job.favourite.remove(user)
        else:
            job.favourite.add(user)
        return Response("Successfull",status=status.HTTP_200_OK)