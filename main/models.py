from django.db import models

class Questions(models.Model):
    def upload_dir(self,filename):
    	path='main/photo/{}'.format(filename)
    	return path
    Q_id=models.CharField(max_length=10)
    Q_text=models.CharField(max_length=100)
    Q_img = models.ImageField(upload_to=upload_dir,null=False,blank=False)
    Q_tag = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.Q_text


