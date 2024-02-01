from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  #blank(application level validation ) and null (database level validation)
    is_completed = models.BooleanField(default=False) #Use "is <name> " to use boolean field

    def __str__(self):
        return f"{self.title}-{self.description}"
