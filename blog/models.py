from django.db import models

# table 1
class Blog(models.Model):
    # fields
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # for debugging
    def __str__(self):
        return self.title