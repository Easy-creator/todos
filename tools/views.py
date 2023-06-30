from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tools.serializers import TodoSerializer
from tools.models import Todo
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from tools.pagination import CustomPagePagination
# Create your views here.
    
class TodoListCreate(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class = CustomPagePagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'title', 'desc','is_complete']
    search_fields = ['title', 'desc']
    ordering_fields = ['id', 'created_at', 'updated_at']
    # url = /?id=3
    queryset = Todo.objects.all()

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
class TodoDetailViews(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user).order_by('-created_at')