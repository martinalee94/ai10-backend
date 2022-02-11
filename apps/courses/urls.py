import os

from django.urls import include, path

from .views import ExerciseCourseList, ExerciseList

urlpatterns = [
    # test api
    path("exerciselist", ExerciseList.as_view(), name="exercise-list"),
    path("courselist", ExerciseCourseList.as_view(), name="course-list"),
]
