from django.db import models

# Create your models here.


class Config(models.Model):
    id = models.AutoField(primary_key=True)

    config = models.TextField(null=False, blank=False)

    date = models.TimeField(auto_now_add=True, null=False, blank=False)


    class Meta:
        managed = False
        db_table = "configs"
