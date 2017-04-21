from django.db import models

# Create your models here.

class Closet(models.Model):
    closetid = models.IntegerField(primary_key=True)
    product1 = models.ForeignKey('Product', related_name='product1', db_column='product1')
    product2 = models.ForeignKey('Product', related_name = 'product2', db_column='product2')
    product3 = models.ForeignKey('Product', related_name = 'product3', db_column='product3')
    product4 = models.ForeignKey('Product', related_name = 'product4', db_column='product4')
    product5 = models.ForeignKey('Product', related_name = 'product5', db_column='product5')
    product6 = models.ForeignKey('Product', related_name = 'product6', db_column='product6')
    product7 = models.ForeignKey('Product', related_name = 'product7', db_column='product7')
    product8 = models.ForeignKey('Product', related_name = 'product8', db_column='product8')
    product9 = models.ForeignKey('Product', related_name = 'product9', db_column='product9')
    product10 = models.ForeignKey('Product', related_name = 'product10', db_column='product10')
    product11 = models.ForeignKey('Product', related_name = 'product11', db_column='product11')
    product12 = models.ForeignKey('Product', related_name = 'product12', db_column='product12')
    product13 = models.ForeignKey('Product', related_name = 'product13', db_column='product13')
    product14 = models.ForeignKey('Product', related_name = 'product14', db_column='product14')
    product15 = models.ForeignKey('Product', related_name = 'product15', db_column='product15')
    product16 = models.ForeignKey('Product', related_name = 'product16', db_column='product16')
    product17 = models.ForeignKey('Product', related_name = 'product17', db_column='product17')
    product18 = models.ForeignKey('Product', related_name = 'product18', db_column='product18')
    product19 = models.ForeignKey('Product', related_name = 'product19', db_column='product19')
    product20 = models.ForeignKey('Product', related_name = 'product20', db_column='product20')
    product21 = models.ForeignKey('Product', related_name = 'product21', db_column='product21')
    product22 = models.ForeignKey('Product', related_name = 'product22', db_column='product22')
    product23 = models.ForeignKey('Product', related_name = 'product23', db_column='product23')
    product24 = models.ForeignKey('Product', related_name = 'product24', db_column='product24')
    product25 = models.ForeignKey('Product', related_name = 'product25', db_column='product25')
    product26 = models.ForeignKey('Product', related_name = 'product26', db_column='product26')
    product27 = models.ForeignKey('Product', related_name = 'product27', db_column='product27')
    product28 = models.ForeignKey('Product', related_name = 'product28', db_column='product28')
    product29 = models.ForeignKey('Product', related_name = 'product29', db_column='product29')
    product30 = models.ForeignKey('Product', related_name = 'product30', db_column='product30')
    product31 = models.ForeignKey('Product', related_name = 'product31', db_column='product31')
    product32 = models.ForeignKey('Product', related_name = 'product32', db_column='product32')
    product33 = models.ForeignKey('Product', related_name = 'product33', db_column='product33')
    product34 = models.ForeignKey('Product', related_name = 'product34', db_column='product34')
    product35 = models.ForeignKey('Product', related_name = 'product35', db_column='product35')
    product36 = models.ForeignKey('Product', related_name = 'product36', db_column='product36')
    product37 = models.ForeignKey('Product', related_name = 'product37', db_column='product37')
    product38 = models.ForeignKey('Product', related_name = 'product38', db_column='product38')
    product39 = models.ForeignKey('Product', related_name = 'product39', db_column='product39')
    product40 = models.ForeignKey('Product', related_name = 'product40', db_column='product40')
    product41 = models.ForeignKey('Product', related_name = 'product41', db_column='product41')
    product42 = models.ForeignKey('Product', related_name = 'product42', db_column='product42')
    product43 = models.ForeignKey('Product', related_name = 'product43', db_column='product43')
    product44 = models.ForeignKey('Product', related_name = 'product44', db_column='product44')
    product45 = models.ForeignKey('Product', related_name = 'product45', db_column='product45')
    product46 = models.ForeignKey('Product', related_name = 'product46', db_column='product46')
    product47 = models.ForeignKey('Product', related_name = 'product47', db_column='product47')
    product48 = models.ForeignKey('Product', related_name = 'product48', db_column='product48')
    product49 = models.ForeignKey('Product', related_name = 'product49', db_column='product49')
    product50 = models.ForeignKey('Product', related_name = 'product50', db_column='product50')
    outfit1 = models.ForeignKey('Outfit', related_name = 'outfit1',db_column='outfit1')
    outfit2 = models.ForeignKey('Outfit',related_name = 'outfit2',db_column='outfit2')
    outfit3 = models.ForeignKey('Outfit',related_name = 'outfit3',db_column='outfit3')
    outfit4 = models.ForeignKey('Outfit',related_name = 'outfit4',db_column='outfit4')
    outfit5 = models.ForeignKey('Outfit',related_name = 'outfit5',db_column='outfit5')
    outfit6 = models.ForeignKey('Outfit',related_name = 'outfit6',db_column='outfit6')
    outfit7 = models.ForeignKey('Outfit',related_name = 'outfit7',db_column='outfit7')
    outfit8 = models.ForeignKey('Outfit',related_name = 'outfit8',db_column='outfit8')
    outfit9 = models.ForeignKey('Outfit', related_name = 'outfit9',db_column='outfit9')
    outfit10 = models.ForeignKey('Outfit',related_name = 'outfit10',db_column='outfit10')

    def __str__(self):
        return self.closetid

    class Meta:
        managed = False
        db_table = 'closets'
        #unique_together = (("ability_name", "char"),)

class Outfit(models.Model):
    outfitid = models.IntegerField(primary_key=True)
    top = models.ForeignKey('Product', related_name = 'top', db_column='top')
    bottom = models.ForeignKey('Product', related_name = 'bottom', db_column='bottom')
    shoes = models.ForeignKey('Product', related_name = 'shoes', db_column='shoes')
    
    def __str__(self):
        return self.outfitid


    class Meta:
        managed = False
        db_table = 'outfits'
        #unique_together = (("char", "alias_name"),) has to do with foreign key??

class Product(models.Model):
    productid = models.IntegerField(db_index=True, primary_key=True)
    productname = models.TextField(db_index=True)
    producttype = models.ForeignKey('Type', db_column='producttype')
    brand = models.TextField(db_index=True)
    color = models.TextField()
    gender = models.CharField(max_length=10)
    price = models.DecimalField(db_index=True, max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    imgurl = models.TextField()

    def __str__(self):
        return self.productname


    class Meta:
        managed = False
        db_table = 'products'
        #unique_together = (("char", "comic"),) ????

class Type(models.Model):
    typename = models.TextField(primary_key=True)
    parenttype = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    occasion = models.CharField(max_length=30)
    
    def __str__(self):
        return self.typename


    class Meta:
        managed = False
        db_table = 'types'
        unique_together = (("typename", "parenttype", "season", "occasion"),)

class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    fname = models.TextField()
    lname = models.TextField()        

    def __str__(self):
        return str(self.fname + self.lname)


    class Meta:
        managed = False
        db_table = 'users'


