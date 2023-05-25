from django.db import models

# Django web applications access and manage data through
# Python objects referred to as models. Models define the structure
# of stored data, including the field types and possibly
# also their maximum size, default values, selection list
# options, help text for documentation, label text for forms,
# etc. The definition of the model is independent of the
# underlying database — you can choose one of several as part
# of your project settings. Once you've chosen what database
# you want to use, you don't need to talk to it directly at
# all — you just write your model structure and other code,
# and Django handles all the dirty work of communicating with
# the database for you.

# When designing your models, it makes sense to have separate
# models for every "object" (a group of related information).


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)

    owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)
    class Meta:
        # order the blog post by created date
        ordering = ['created']