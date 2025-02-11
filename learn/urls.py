from django.contrib import admin
from django.urls import path, include  # Fixed import of 'include'
from accounts.views import RegisterView, LoginView
from courses import urls as courses_urls  # Correct the import alias for courses app
from courses.views import CourseCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include(courses_urls)),  # Corrected to include courses app's URLs
    path('create/', CourseCreateView.as_view(), name='course_create'),

]
