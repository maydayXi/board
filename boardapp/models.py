from django.db import models

# Create your models here.

class BoardUnit(models.Model):
    b_name = models.CharField(max_length=20, null=False)
    b_gender = models.CharField(max_length=2, default='m', null=False)
    b_title = models.CharField(max_length=100, null=False)
    b_time = models.DateTimeField(auto_now=True)
    b_mail = models.EmailField(max_length=100, blank=True, default='')
    b_web = models.URLField(max_length=200, blank=True, default='')
    b_content = models.TextField(null=False)
    b_response = models.TextField(blank=True, default='')

    def __str__(self):
        return self.b_title
