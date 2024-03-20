import graphene
from graphene_django import DjangoObjectType

from Courses.models import Courses, Lesson
from Users.models import CustomUser


class StudentType(DjangoObjectType):
    class Meta:
        model = CustomUser


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson


class CourseType(DjangoObjectType):
    students = graphene.List(StudentType)
    lessons = graphene.List(LessonType)

    class Meta:
        model = Courses

    def resolve_students(self, info):
        return self.students.all()

    def resolve_lessons(self, info):
        return self.lesson_set.all()


class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)

    def resolve_all_courses(self, info, **kwargs):
        return Courses.objects.all()


schema = graphene.Schema(query=Query)
