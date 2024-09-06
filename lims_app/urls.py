"""
URL configuration for lims_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('readers', ReaderListCreateAPIView.as_view()),
    path('readers/<int:pk>', ReaderDetailAPIView.as_view()),
    path('readers/<int:pk>/update', ReaderUpdateAPIView.as_view()),
    path('readers/<int:pk>/delete', ReaderDestroyAPIView.as_view()),
    path('books', BookListCreateAPIView.as_view()),
    path('books/<int:pk>', BookDetailAPIView.as_view()),
    path('books/<int:pk>/update', BookUpdateAPIView.as_view()),
    path('books/<int:pk>/delete', BookDestroyAPIView.as_view()),
    # path('export_all', export_all_data, name = 'export_all_data'),
    # path('export_pkl', export_pkl, name = 'export_pkl'),
    # path('import_all', import_all_data, name='import_all_data'),
    # path('import_pkl', import_pkl, name='import_pkl'),
]
