from django.db import models

# Create your models here.


class Closet(models.Model):
    closetId = models.IntegerField(primary_key=True)
    product1 = models.ForeignKey('Product')
    product2 = models.ForeignKey('Product')
    product3 = models.ForeignKey('Product')
    product4 = models.ForeignKey('Product')
    product5 = models.ForeignKey('Product')
    product6 = models.ForeignKey('Product')
    product7 = models.ForeignKey('Product')
    product8 = models.ForeignKey('Product')
    product9 = models.ForeignKey('Product')
    product10 = models.ForeignKey('Product')
    product11 = models.ForeignKey('Product')
    product12 = models.ForeignKey('Product')
    product13 = models.ForeignKey('Product')
    product14 = models.ForeignKey('Product')
    product15 = models.ForeignKey('Product')
    product16 = models.ForeignKey('Product')
    product17 = models.ForeignKey('Product')
    product18 = models.ForeignKey('Product')
    product19 = models.ForeignKey('Product')
    product20 = models.ForeignKey('Product')
    product21 = models.ForeignKey('Product')
    product22 = models.ForeignKey('Product')
    product23 = models.ForeignKey('Product')
    product24 = models.ForeignKey('Product')
    product25 = models.ForeignKey('Product')
    product26 = models.ForeignKey('Product')
    product27 = models.ForeignKey('Product')
    product28 = models.ForeignKey('Product')
    product29 = models.ForeignKey('Product')
    product30 = models.ForeignKey('Product')
    product31 = models.ForeignKey('Product')
    product32 = models.ForeignKey('Product')
    product33 = models.ForeignKey('Product')
    product34 = models.ForeignKey('Product')
    product35 = models.ForeignKey('Product')
    product36 = models.ForeignKey('Product')
    product37 = models.ForeignKey('Product')
    product38 = models.ForeignKey('Product')
    product39 = models.ForeignKey('Product')
    product40 = models.ForeignKey('Product')
    product41 = models.ForeignKey('Product')
    product42 = models.ForeignKey('Product')
    product43 = models.ForeignKey('Product')
    product44 = models.ForeignKey('Product')
    product45 = models.ForeignKey('Product')
    product46 = models.ForeignKey('Product')
    product47 = models.ForeignKey('Product')
    product48 = models.ForeignKey('Product')
    product49 = models.ForeignKey('Product')
    product50 = models.ForeignKey('Product')
    outfit1 = models.ForeignKey('Outfit')
    outfit2 = models.ForeignKey('Outfit')
    outfit3 = models.ForeignKey('Outfit')
    outfit4 = models.ForeignKey('Outfit')
    outfit5 = models.ForeignKey('Outfit')
    outfit6 = models.ForeignKey('Outfit')
    outfit7 = models.ForeignKey('Outfit')
    outfit8 = models.ForeignKey('Outfit')
    outfit9 = models.ForeignKey('Outfit')
    outfit10 = models.ForeignKey('Outfit')

    class Meta:
        managed = False
        db_table = 'closets'
        #unique_together = (("ability_name", "char"),)

class Outfit(models.Model):
    outfitId = models.IntegerField(primary_key=True)
    top = models.ForeignKey('Product')
    bottom = models.ForeignKey('Product')
    shoes = models.ForeignKey('Product')

    class Meta:
        managed = False
        db_table = 'outfits'
        #unique_together = (("char", "alias_name"),) has to do with foreign key??

class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.TextField()
    productType = models.ForeignKey('Type')
    brand = models.TextField()
    color = models.TextField()
    gender = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    imgUrl = models.TextField()

    class Meta:
        managed = False
        db_table = 'products'
        #unique_together = (("char", "comic"),) ????

class Type(models.Model):
    typeName = models.TextField(primary_key=True)
    parentType = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    occasion = models.CharField(max_length=30)
    
    class Meta:
        managed = False
        db_table = 'types'
        unique_together = (("typeName", "parentType", "season", "occasion"),)

class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    fName = models.TextField()
    lName = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'


