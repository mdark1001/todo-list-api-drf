"""
"""

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from users.views import UserView
router =DefaultRouter()

router.register(r'users',UserView,basename='users')
urlpatterns = [
      path('', include(router.urls))
]
