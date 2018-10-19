'''
Created on 2018/10/17

@author: t16cs015
'''

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('<int:question_id>/', views.detail, name='details'),
    
    path('<int:question_id>/results/', views.results, name='results'),
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    #test
    ]