from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Courses
from .forms import CoursesForm


class CourseListView(ListView):
    model = Courses
    context_object_name = 'courses'
    template_name = 'courses.html'


class CourseDetailView(DetailView):
    model = Courses
    template_name = 'course_detail.html'


class CourseCreateView(CreateView):
    model = Courses
    template_name = 'course_create_form.html'
    form_class = CoursesForm
    success_url = '/course/list/'


class CourseUpdateView(UpdateView):
    model = Courses
    template_name = 'course_create_form.html'
    form_class = CoursesForm
    success_url = '/course/list/'


class CourseDeleteView(DeleteView):
    model = Courses
    template_name = 'course_confirm_delete.html'
    success_url = '/course/list/'
