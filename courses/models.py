from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='courses', 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


    class Meta:
        permissions = [
            ('can_create_course', 'Can create courses'),
            ('can_view_course', 'Can view courses'),
            ('can_enroll_course', 'Can enroll in courses'),
        ]

    def __str__(self):
        return self.title
