from django.db import models
import uuid
# Create your models here.


class Menu(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name= models.CharField(max_length=150)
    item_description=models.TextField()
    item_image=models.ImageField(upload_to="item")
    item_price=models.IntegerField(default=0)
    num_pieces=models.IntegerField(default=0)
    item_type=models.CharField(max_length=150,default='NA')

    def __str__(self):
        return str(self.item_name)