from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import  csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status


# https://www.django-rest-framework.org/api-guide/renderers/

from posts.models import Post
from posts.serializers import PostSerializer

# when the posts requested from the API we need to get
# that back and we can also request or update individual post
# which requires post id

#     GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
#     POST — Creates a new record that gets appended to the database
#     PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
#     DELETE — Deletes the record at the given URI
#     PATCH — Update individual fields of a record

@api_view(['GET', 'POST'])
def post_list(request, format=None):
    # if there is get request, all posts needs to be get, serialized
    # and needs to be returned as JSON.

    # if there is post request, JSON data needs to be parsed,
    # serialized and if the data is valid it needs to be saved
    # and JSON response as success needs to be returned.
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# details for the individual posts
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk, format=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)