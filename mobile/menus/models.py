from django.db import models

from users.models import CustomUser

# Create your models here.


class News(models.Model):
    news_link=models.CharField(max_length=20,blank=False,null=False)
    featured_image=models.ImageField(blank=False,null=False,max_length=100,upload_to="news/images")
    title=models.CharField(blank=False,null=False,max_length=100)
    title_description=models.CharField(blank=False,null=False,max_length=100)
    content=models.CharField(blank=False,null=False,max_length=1000)
    content_image=models.ImageField(blank=False,null=False,max_length=100,upload_to="news/images/contentImage")
    content_image2=models.ImageField(blank=False,null=False,max_length=100,upload_to="news/images/contentImage2")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Activities(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image=models.ImageField(blank=False,null=False,max_length=100,upload_to="activities")
    content=models.CharField(blank=False,null=False,max_length=1000)
    likes_count=models.IntegerField(blank=False,default=0)
    comments_count=models.IntegerField(blank=False,default=0)
    locked_comments=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class ActivitiesComment(models.Model):
    activity=models.ForeignKey(Activities,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True,max_length=100,upload_to="activities/comment")
    content=models.CharField(blank=False,null=False,max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class ActivitiesLike(models.Model):
    activity=models.ForeignKey(Activities,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.activity)


class BlockedActivities(models.Model):
    activity=models.ForeignKey(Activities,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.activity)

class SavedActivities(models.Model):
    activity=models.ForeignKey(Activities,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.activity)