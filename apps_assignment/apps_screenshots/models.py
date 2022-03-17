from django.db import models

# Create your models here.
"""Assumed that auto id field would be enough even if datas in csv files has id fields """
class Apps(models.Model):
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to= 'images/', max_length=1000) #This can be changed to ImageField !!Search which is more appropiate.
    created_at = models.DateTimeField(auto_now_add=True) # I assume that this field should be entered automatically.
    updated_at = models.DateTimeField(auto_now=True) # This one also changed automatically when model updated.

    def __str__(self):
        return self.name

class Screenshots(models.Model):
    app_id = models.ForeignKey(Apps, on_delete=models.CASCADE) #Decide deletion model in future
    file_name = models.ImageField(upload_to= 'images/', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True) # I assume that this field should be entered automatically.
    updated_at = models.DateTimeField(auto_now=True) # This one also changed automatically when model updated.

    def __str__(self):
        return (self.app_id.name + "\'s  " + str(self.file_name) )