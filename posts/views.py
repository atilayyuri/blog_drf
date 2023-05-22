from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import  csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

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

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # if there is get request, all posts needs to be get, serialized
    # and needs to be returned as JSON.

    # if there is post request, JSON data needs to be parsed,
    # serialized and if the data is valid it needs to be saved
    # and JSON response as success needs to be returned.

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = PostSerializer(data=request)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)

    # def get_object(self, pk):
    #     try:
    #         return Post.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post, data=request)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
