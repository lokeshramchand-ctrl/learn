from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsAdminOrInstructor

class CourseCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrInstructor]

    def post(self, request):
        # Create course logic here
        course = Course.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            instructor=request.user
        )
        return Response({"message": "Course created successfully!"}, status=status.HTTP_201_CREATED) # type: ignore
