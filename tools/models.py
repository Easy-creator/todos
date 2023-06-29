from django.db import models
from users.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-created_at']