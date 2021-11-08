"""


"""
from django.urls import path
from todo_list.views import TaskListView,TaskUpdateRetrieveView
app_name='tasks'

urlpatterns = [
    path('task/',TaskListView.as_view(),name='list'),
    path(r'task/(?P<slug>[a-zA-Z0-9_-]+)',TaskUpdateRetrieveView.as_view(),name='update'),
    
]