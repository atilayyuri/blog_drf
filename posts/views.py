from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser



from posts.models import Post
from posts.serializers import PostSerializer

# when the posts requested from the API we need to get
# that back and we can also request or update individual post
# which requires post id

@csrf_exempt
def post_list(request):
    # if there is get request, all posts needs to be get, serialized
    # and needs to be returned as JSON.

    # if there is post request, JSON data needs to be parsed,
    # serialized and if the data is valid it needs to be saved
    # and JSON response as success needs to be returned.
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)


    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# details for the individual posts
@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)