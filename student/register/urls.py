from django.urls import path
from .import views
urlpatterns=[
    
    path('',views.home),
    path('table',views.table,name='table'),
    path('insert',views.insert,name='insert'),
    path('update/<int:up>',views.update,name='update'),
    path('updatepage/<int:up>',views.updatepage,name='updatepage'),
    path('delete/<int:up>',views.delete,name='delete'),
    path('deletepage/<int:up>',views.deletepage,name='deletepage'),
]