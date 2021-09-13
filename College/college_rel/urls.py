from django.urls import path
from .views import AddLecturerView, AddStudentView, AdddepartmentView, DeleteLecturerView, DeleteStudentView, Homeview, Lecturerview, Searchview, ShowLecturerView, ShowStudentView, Showdepartmentview, Studentview, UpdateLecturerView, UpdateStudentView


urlpatterns=[
    path('adddep/',AdddepartmentView,name='Adddepartment'),
    path('addstu/',AddStudentView,name='Addstudent'),
    path('addlec/',AddLecturerView,name='Addlecturer'),
    path('showdep/',Showdepartmentview,name='Showdepartment'),
    path('showstu/',ShowStudentView,name='Showstudent'),
    path('showlec/',ShowLecturerView,name='Showlecturer'),
    path('updatestu/<int:update>',UpdateStudentView,name='Updatestudent'),
    path('updatelecturer/<int:update>',UpdateLecturerView,name='Updatelecturer'),
    path('deletestu/<int:delete>',DeleteStudentView,name='Deletestudent'),
    path('deletelecturer/<int:delete>',DeleteLecturerView,name='Deletelecturer'),
    path('search/',Searchview,name='Search'),
    path('home/',Homeview,name='Home'),
    path('stu/',Studentview,name='Student'),
    path('lec/',Lecturerview,name='Lecturer'),
    



]
