from django.db import models
from django.contrib.auth.models import User
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from  embed_video.fields  import  EmbedVideoField

#Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=200, unique=True)
    uploader = models.ForeignKey(User, on_delete= models.CASCADE, related_name='collections')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    video = EmbedVideoField()
    created_on = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    likes = models.ManyToManyField(User, related_name='collection_like')
    dislikes= models.ManyToManyField(User, related_name='collection_dislike')

    class Meta:
        verbose_name_plural = "Collection"

    def __str__(self):
        return self.title if  self.title  else  " "
    
    def number_of_likes(self):
        return self.likes.count()

    def user_likes(self):
        return self.likes

    def number_of_dislikes(self):
        return self.dislikes.count()

    def user_dislikes(self):
        return self.dislikes

