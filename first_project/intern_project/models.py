from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class chaiVarity(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL' , 'KIWI'),
        ('PL' , 'PLAIN'),
        ('EL' , 'ELACHI')
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)


    def __str__(self):
        return self.name
    
# one to many
class ChaiReviews(models.Model):
    chai = models.ForeignKey(chaiVarity,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.IntegerField(max_length=5)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for chai {self.chai.name}'
    
# many to many relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # here we can dirctly tell to django that it is a many to many field with chaivarity class
    chai_varity = models.ManyToManyField(chaiVarity,related_name='store')

    def __str__(self):
        return self.name
    

# one to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate For {self.name.chai}'