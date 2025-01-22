from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateView.as_view()),
    path("lessons/<int:pk>/", LessonRetrieveUpdateDestroyView.as_view()),
]
