from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    parent = models.CharField(max_length=255)
    relative_url = models.CharField(max_length=255)
    full_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'main_menu'

    def __str__(self):
        return self.title
    
    @classmethod
    def get_table(cls, table_name):
        cls._meta.db_table = table_name
        return cls.objects.using('default')