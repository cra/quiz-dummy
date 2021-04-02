"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('q/<slug:quiz_slug>', views.quiz_start, name='quiz-start'),
    path(
        'q/<slug:quiz_slug>/<uuid:user_uuid>/<int:section_part>',
        views.quiz_section,
        name='quiz-section'),
    path(
        'q/<slug:quiz_slug>/<uuid:user_uuid>/<int:section_part>/score',
        views.quiz_section_score,
        name='quiz-section-score'),
    path(
        'q/<slug:quiz_slug>/<uuid:user_uuid>/final',
        views.quiz_section_final,
        name='quiz-section-final'),
    path(
        'q/<slug:quiz_slug>/<uuid:user_uuid>/clear-it-please',
        views.quiz_clear_user_result,
        name='quiz-clear-user-result'),
    # path('admin/', admin.site.urls),
]
