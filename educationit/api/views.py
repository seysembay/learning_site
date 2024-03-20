from rest_framework import generics, status
from rest_framework.response import Response
from Courses.models import Courses, Lesson
from Users.models import CustomUser
from .permissions import IsSuperuserOrReadOnly, OnlyForMe
from .serializers import CourseSerializer, LessonSerializer


class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class CourseAddStudentAPIView(generics.UpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        student_id = request.data.get('student_id')
        if student_id:
            try:
                student = CustomUser.objects.get(id=student_id)
                instance.students.add(student)
                instance.save()
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            except:
                return Response({'detail': 'Student with specified id does not exist.'},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'Please provide student_id.'}, status=status.HTTP_400_BAD_REQUEST)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [OnlyForMe]


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [OnlyForMe]
