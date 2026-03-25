#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render    
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging


from .models import Course
from .models import Post

logger = logging.getLogger('django')

class HelloApiView(APIView):
    def get(self, request):
        my_name = request.GET.get('name', None)
        if my_name:
            retValue = {}
            retValue['data'] = "WHAT'S UP" + my_name
            return Response(retValue, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "parameter: name is None"},
                status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['POST'])
def add_post(request):
    title = request.GET.get('title' , '')
    content = request.GET.get('content' , '')
    photo = request.GET.get('photo' , '')
    location = request.GET.get('location' , '')

    new_post = Post()
    new_post.title = title
    new_post.content = content
    new_post.photo = photo
    new_post.location = location
    new_post.save()
    logger.debug(" *********************** myhello_api: " + title)
    if title:
        return Response({"data": title + "insert!"}, status=status.HTTP_200_OK)
    else:
        return Response({"res": "parameter: name is None"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_post(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False)

    #return Response({"data": 
     #                json.dumps(
      #                   list(posts),
       #                  sort_keys=True,
        #                 indent=1,
         #                cls=DjangoJSONEncoder)},
          #               status=status.HTTP_200_OK)

@api_view(['GET'])
def addcourse_post(request):
    course_title = request.GET.get('course_title', '')
    department = request.GET.get('department', '')
    instructor = request.GET.get('instructor', '')

    new_course = Course()
    new_course.course_title = course_title
    new_course.department = department
    new_course.instructor = instructor
    new_course.save()

    logger.debug("*********************** myhello_api: " + course_title)

    if course_title:
        return Response({"data": course_title + " insert!"}, status=status.HTTP_200_OK)
    else:
        return Response({"res": "parameter: course_title is None"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def courselist_post(request):
    course_post = Course.objects.all().values()
    return JsonResponse(list(course_post), safe=False)

    #return Response({"data": 
     #                json.dumps(
      #                   list(posts),
       #                  sort_keys=True,
        #                 indent=1,
         #                cls=DjangoJSONEncoder)},
          #               status=status.HTTP_200_OK)
def course_list_page(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})