from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    id = models.IntegerField(primary_key=True, auto_created=True)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User)
    content = models.TextField()
    title = models.CharField(max_length=30)
    date = models.DateTimeField(verbose_name='Created on', auto_now_add=True)

    def __unicode__(self):
        return self.title