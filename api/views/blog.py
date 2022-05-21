from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, permissions,status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.blog import Blog
from api.serializers.blog import BlogDetailSerializer,BlogCreateSerializer,BlogListSerializer,BlogListUserSerializer
from api.views.paginations import BlogPageNumberPagination
from api.serializers.taggit import TagSerializer
from taggit.models import Tag


class TagListAPIView(ListAPIView):
    queryset = Blog.tags.most_common()[:5]
    serializer_class = TagSerializer


class BlogListCreateAPIView(ListCreateAPIView):
    queryset = Blog.objects.filter(approved=True)
    pagination_class = BlogPageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['approved','tags__name']
    search_fields = ['title', 'tags__name','content'] 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogCreateSerializer
        return BlogListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self,serializer):
        instance = serializer.save(author=self.request.user)
        if 'tags' not in serializer.validated_data:
            instance.tags.set("Others")

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'


class BlogByUserAPIView(ListAPIView):
    serializer_class = BlogListUserSerializer

    def get_queryset(self):
        return Blog.objects.filter(author__username=self.kwargs['username'])


class BlogLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self,request,blog_id):
        user = request.user
        blog = get_object_or_404(Blog,id=blog_id)
        if blog.liked_by.filter(id=user.id).exists():
            blog.liked_by.remove(user)
        else:
            blog.liked_by.add(user)
        return Response("Successfull",status=status.HTTP_200_OK)