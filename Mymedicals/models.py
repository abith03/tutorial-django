from django.db import models

# Create your models here.
from django.db import models 


# Create your models here.
class medicine(models.Model):
    name= models.CharField(max_length=200)
    type= models.CharField( max_length=200,default='')
    price=models.DecimalField( max_digits=5, decimal_places=2 ,default=False)
    Mfg_date=models.DateField(null=True, blank=True)
    Exp_date=models.DateField(null=True, blank=True)


    
    def str(self):
        return self.name