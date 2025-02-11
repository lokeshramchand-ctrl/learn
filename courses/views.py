from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Course, Module, Enrollment, Assignment, Submission
from .serializers import CourseSerializer, ModuleSerializer, EnrollmentSerializer, AssignmentSerializer, SubmissionSerializer
from .permissions import IsInstructor, IsStudent, IsAdminOrInstructor, IsAdminOnly


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrInstructor]  # Only admins or instructors can create courses

    def perform_create(self, serializer):
        # Assign the instructor as the user who created the course
        if self.request.user.is_authenticated:
            serializer.save(instructor=self.request.user)

    def get_queryset(self):
        # Allow listing for all authenticated users
        return Course.objects.all()


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudent]  # Only students can enroll

    def perform_create(self, serializer):
        user = self.request.user
        course = serializer.validated_data['course']
        
        # Prevent instructors from enrolling in their own courses
        if user != course.instructor:
            serializer.save(user=user)
        else:
            raise PermissionError('Instructor cannot enroll in their own course.')


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAdminOrInstructor]  # Only admins or instructors can create assignments

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(course=self.request.data['course'])
        else:
            raise PermissionError('Only instructors or admins can create assignments.')


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsStudent]  # Only students can submit assignments

    def perform_create(self, serializer):
        user = self.request.user
        assignment = serializer.validated_data['assignment']
        
        # Ensure that the student is enrolled in the course for the assignment
        if Enrollment.objects.filter(user=user, course=assignment.course).exists():
            serializer.save(user=user)
        else:
            raise PermissionError('You must be enrolled in the course to submit an assignment.')

    def update(self, request, *args, **kwargs):
        submission = self.get_object()
        
        # Allow instructors or admins to grade submissions
        if request.user.is_authenticated and (request.user.is_staff or request.user == submission.assignment.course.instructor):
            return super().update(request, *args, **kwargs)
        else:
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
