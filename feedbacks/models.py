
from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 220)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.subject