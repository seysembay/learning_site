from django.urls import path
from .views import CourseListView, CourseCreateView, CourseDetailView, CourseUpdateView, CourseDeleteView
app_name = 'Courses'
urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
]
