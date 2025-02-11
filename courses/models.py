from django.db import models
from django.contrib.auth.models import User

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('can_create_course', 'Can create courses'),
            ('can_view_course', 'Can view courses'),
            ('can_enroll_course', 'Can enroll in courses'),
        ]
    
    def __str__(self):
        return self.title

# Module Model
class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.FileField(upload_to='modules/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.title}'

# Assignment Model
class Assignment(models.Model):
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    submission_deadline = models.DateTimeField()

    def __str__(self):
        return self.title

# Submission Model
class Submission(models.Model):
    user = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, related_name='submissions', on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='submissions/%Y/%m/%d/')
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.assignment.title} submission'
