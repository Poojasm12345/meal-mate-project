from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    mobile = models.CharField(max_length = 20) 
    address = models.TextField(max_length = 20)

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length = 200, default="https://www.google.com/imgres?q=RESTAURANT%20IMAGE&imgurl=https%3A%2F%2Ft3.ftcdn.net%2Fjpg%2F03%2F24%2F73%2F92%2F360_F_324739203_keeq8udvv0P2h1MLYJ0GLSlTBagoXS48.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Drestaurant&docid=6wKZbq7KClHX9M&tbnid=F_Q6WmgH6OKsSM&vet=12ahUKEwjh--j1-t6PAxX4oWMGHSKAAYMQM3oECBcQAA..i&w=586&h=360&hcb=2&ved=2ahUKEwjh--j1-t6PAxX4oWMGHSKAAYMQM3oECBcQAA")
    cuisine = models.CharField(max_length = 20)
    rating = models.FloatField()

    
