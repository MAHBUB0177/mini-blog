from django.db import models

class Post(models.Model):
  title=models.CharField(max_length=20,blank=True,null=True)
  Desc=models.CharField(max_length=20)

class Products_Packet_Mapping(models.Model):
    product_id = models.CharField(max_length=20, null=False, blank=True)
    packet_product_id = models.CharField(max_length=20, null=False, blank=True)
    quantity_ratio = models.IntegerField(null=True)
    app_user_id = models.CharField(max_length=20, null=False)
    app_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id
class Supplier_Information(models.Model):
    supp_id = models.CharField(max_length=20, primary_key=True)
    branch_code = models.IntegerField(blank=True)
    supp_name = models.CharField(max_length=100, null=False)
    proprietor_name = models.CharField(max_length=100, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=False)
    account_number = models.CharField(max_length=20, null=True, blank=True)
    supp_address = models.CharField(max_length=300, null=True, blank=True)
    supp_mobile = models.CharField(max_length=20, null=True)
    supp_email = models.CharField(max_length=100, null=True, blank=True)
    supp_web = models.CharField(max_length=100, null=True, blank=True)
    supp_key_person = models.CharField(max_length=100, null=True, blank=True)
    supp_fax = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_deleted = models.BooleanField(blank=True, default=False)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.supp_name)



class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
      return str(self.album_name)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks1', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    # class Meta:
    #     unique_together = ['album', 'order']
    #     ordering = ['order']
    def __str__(self):
        return '%d: %s' % (self.order, self.title)


class Product_Categories(models.Model):
    categories_id = models.CharField(
        max_length=20,  blank=True, primary_key=True)
    categories_name = models.CharField(max_length=200, null=False)
    image_class_name = models.CharField(max_length=200, null=True,blank=True)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categories_name

class Products(models.Model):
    product_id = models.CharField(
        max_length=20, null=False, blank=True, primary_key=True)
    category_id = models.ForeignKey(Product_Categories, on_delete=models.PROTECT,
                                    related_name='product_category', db_column='category_id')
    product_name = models.CharField(max_length=200)
    product_model = models.CharField(max_length=200, blank=True, null=True)
    product_group = models.CharField(max_length=200, blank=True, null=True)
    product_price = models.DecimalField(
        max_digits=22, decimal_places=2, default=0.00, blank=True, null=True)
    discount_amount = models.DecimalField(
        max_digits=22, decimal_places=2, default=0.00, blank=True, null=True)
    product_old_price = models.DecimalField(
        max_digits=22, decimal_places=2, default=0.00, blank=True, null=True)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_name) +""+ str(self.product_model)


###many to many #######


class rating_Manager(models.Manager):
    def rating(self):
        return self.filter(num_stars='3')


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Albums(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE,related_name="album_name",db_column='artist')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    musician=models.ManyToManyField(Musician)

    objects=rating_Manager()
    def __str__(self):
        return str(self.name)


####### model manager ######

class DocumentManager(models.Manager):
    def pdfs(self):
        return self.filter(file_type='pdf')

    def smaller_than(self, size):
        return self.filter(size__lt=size)
    
    
    def smaller_than1(self, size):
        return self.filter(age__lt=size)


class Document(models.Model):
    name = models.CharField(max_length=30)
    size = models.PositiveIntegerField(default=0)
    file_type = models.CharField(max_length=10, blank=True)

    objects1 = DocumentManager()

    def __str__(self) -> str:
        return self.name
        

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=10, blank=True)

    objects1 = DocumentManager()

    def __str__(self) -> str:
        return self.name