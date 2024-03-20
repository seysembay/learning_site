from django.urls import path
from .views import CourseListAPIView, CourseRetrieveUpdateDestroyAPIView, CourseAddStudentAPIView, \
    LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail'),
    path('courses/<int:pk>/add_student/', CourseAddStudentAPIView.as_view(), name='course-add-student'),
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-detail'),
]
