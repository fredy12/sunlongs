import os

from django.db import models
from django import forms

# Create your models here.

class CompanyInfo(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=20, null=True, blank=True)  # chinese or english
    short_name = models.CharField(max_length=50, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    abstract = models.CharField(max_length=500, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    culture = models.TextField(null=True, blank=True)
    application = models.TextField(null=True, blank=True)
    business = models.TextField(null=True, blank=True)
    certificate_info = models.TextField(null=True, blank=True)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    contact_name = models.CharField(max_length=20, null=True, blank=True)
    order_num = models.CharField(max_length=20, null=True, blank=True)
    fax_num = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = website = models.URLField(null=True, blank=True)
    additional = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ArticleInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    type = models.CharField(max_length=50, null=True, blank=True)   # home, company, product, news, customer, contact
    tag = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ImageInfo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='pic')
    display_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super(ImageInfo, self).delete(*args,**kwargs)


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    introduction = models.CharField(max_length=500, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ProductInfo(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=20, null=True, blank=True)  # chinese or english
    type = models.ForeignKey(ProductType)
    standard = models.CharField(max_length=50, null=True, blank=True)
    market = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    pic = models.ImageField(upload_to='product', null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    power = models.CharField(max_length=20, null=True, blank=True)
    flow = models.CharField(max_length=20, null=True, blank=True)
    head = models.CharField(max_length=20, null=True, blank=True)
    voltage = models.CharField(max_length=20, null=True, blank=True)
    outlet = models.CharField(max_length=20, null=True, blank=True)
    speed = models.CharField(max_length=20, null=True, blank=True)
    eff = models.CharField(max_length=20, null=True, blank=True)
    abstract = models.CharField(max_length=500, null=True, blank=True)
    feature = models.CharField(max_length=500, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.pic.path):
            os.remove(self.pic.path)

        super(ProductInfo, self).delete(*args,**kwargs)


class NewsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=20, null=True, blank=True)  # chinese or english
    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    type = models.CharField(max_length=50, null=True, blank=True)   # home, company, product, news, customer, contact
    tag = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class ArticleInfoForm(forms.ModelForm):
    class Meta:
        model = ArticleInfo
        fields = '__all__'


class ImageInfoForm(forms.ModelForm):
    class Meta:
        model = ImageInfo
        fields = '__all__'


class ProductInfoForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = '__all__'

    def save_with_delete_old_pic(self, old_pic_path):
        if os.path.isfile(old_pic_path):
            os.remove(old_pic_path)
        self.save()


class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'


class NewsInfoForm(forms.ModelForm):
    class Meta:
        model = NewsInfo
        fields = '__all__'
