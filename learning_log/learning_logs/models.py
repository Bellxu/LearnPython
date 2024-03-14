from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """""用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=CASCADE)
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.text
class Entry(models.Model):
    """""学习到有关某个主题的具体知识"""
    topic=models.ForeignKey(Topic,on_delete=CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self) -> str:
        return self.text[:50]+"..."    
    
User.objects.all()
for user in User.objects.all():
    print(user.username,user.id)