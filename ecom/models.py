from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    CATEGORIES = (
        ('Electronics','Electronics'),
        ('Fashion','Fashion'),
        ('Home','Home'),
        ('Beauty','Beauty'),
        ('Books','Books'),
        ('Sports','Sports'),
        ('Others','Others'),
    )
    name=models.CharField(max_length=120)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.TextField()
    about=models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='Others')
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField(default=10)
    
    @property
    def about_list(self):
        if self.about:
            return [line.strip() for line in self.about.split('\n') if line.strip()]
        return []

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS, default='Pending')
    total_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.customer} - {self.product} ({self.quantity})"


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'product')

    def __str__(self):
        return f"{self.customer} - {self.product}"


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'product')

    def __str__(self):
        return f"{self.customer} rated {self.product} - {self.rating}/5"


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(default=10)
    active = models.BooleanField(default=True)
    expiry = models.DateField(null=True, blank=True)
    usage_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.code} ({self.discount_percent}%)"


class Complaint(models.Model):
    COMPLAINT_TYPES = (
        ('Product Quality', 'Product Quality'),
        ('Delivery', 'Delivery'),
        ('Wrong Item', 'Wrong Item'),
        ('Damaged', 'Damaged'),
        ('Other', 'Other'),
    )
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Resolved', 'Resolved'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='complaints')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='complaints')
    complaint_type = models.CharField(max_length=50, choices=COMPLAINT_TYPES, default='Other')
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.complaint_type} ({self.status})"
