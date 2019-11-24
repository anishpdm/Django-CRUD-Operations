from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('',views.facultypage,name='index'),
    path('view',views.indexpage,name='library'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)



    

]