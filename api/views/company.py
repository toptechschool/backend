from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import filters, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.company import CompanyDetailSerializer,CompanyListSerializer,CompanyCreateSerializer
from api.views.paginations import CompanyPageNumberPagination
from api.models import Company


class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    pagination_class = CompanyPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address','description','title'] 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyCreateSerializer
        return CompanyListSerializer


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    lookup_field = 'slug'


class CompanyLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self,request,company_id):
        user = request.user
        company = get_object_or_404(Company,id=company_id)
        if company.follower.filter(id=user.id).exists():
            company.follower.remove(user)
        else:
            company.follower.add(user)
        return Response("Successfull",status=status.HTTP_200_OK)