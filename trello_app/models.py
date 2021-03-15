from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class TaskList(models.Model):
    name = models.TextField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    


class Tasks(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    # user1 = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('P', 'PENDING'),
        ('C', 'COMPLETED'),
        ('IP', 'IN_PROGRESS'),
        ('D', 'DROPPED'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[2], max_length=2)
    def __str__(self):
        return f"{self.content}-{self.task_list}"