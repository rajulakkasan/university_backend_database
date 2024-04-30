from django.urls import path
from readdb.views import home_view, logout_view
from . import views

urlpatterns = [
    # data routes
    path('roster/', views.roster_view, name='roster'),
    path('salary/', views.salary_view, name='salary'),
    path('performance/', views.performance_view, name='performance'),
    path('course_sections/', views.course_sections_view, name='course_sections'),
    path('enrolled_students/', views.enrolled_students_view, name='enrolled_students'),
    path('dept_sections/', views.dept_sections_view, name='dept_sections'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('unauthorized', views.unauthorized_view, name='unauthorized')
    
]


