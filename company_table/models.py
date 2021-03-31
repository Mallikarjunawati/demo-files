from django.db import models

# Create your models here.

class company_table(models.Model):
    company_id=models.IntegerField()
    company_name=models.CharField(null=False , max_length=50)

    class Meta:
        db_table="company_table"