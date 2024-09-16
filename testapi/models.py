from django.db import models

# Create your models here.

class ToDoModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    note = models.CharField(max_length=1500)
    created_on = models.DateTimeField(auto_now_add=True)
    happened_on = models.DateTimeField()

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title