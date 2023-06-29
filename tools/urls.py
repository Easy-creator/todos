from django.urls import path
from tools.views import TodoListCreate, TodoDetailViews

urlpatterns = [
    path('create_details/', TodoListCreate.as_view(), name='create_details'),
    path('update/<int:id>/', TodoDetailViews.as_view(), name='update'),
]