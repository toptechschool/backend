from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, permissions,status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.note import Note
from api.serializers.note import NoteDetailSerializer,NoteCreateSerializer,NoteListSerializer,NoteListUserSerializer
from api.views.paginations import NotePageNumberPagination
from api.serializers.taggit import TagSerializer
from taggit.models import Tag


class TagListAPIView(ListAPIView):
    queryset = Note.tags.most_common()[:5]
    serializer_class = TagSerializer


class NoteListCreateAPIView(ListCreateAPIView):
    queryset = Note.objects.filter(approved=True)
    pagination_class = NotePageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['approved','tags__name']
    search_fields = ['title', 'tags__name','content'] 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NoteCreateSerializer
        return NoteListSerializer

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

class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
    lookup_field = 'slug'


class NoteByUserAPIView(ListAPIView):
    serializer_class = NoteListUserSerializer

    def get_queryset(self):
        return Note.objects.filter(author__username=self.kwargs['username'])


class NoteLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self,request,note_id):
        user = request.user
        note = get_object_or_404(Note,id=note_id)
        if note.liked_by.filter(id=user.id).exists():
            note.liked_by.remove(user)
        else:
            note.liked_by.add(user)
        return Response("Successfull",status=status.HTTP_200_OK)



