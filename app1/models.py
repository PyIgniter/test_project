from django.db import models

# Create your models here.

class Order(models.Model):
    """docstring for Order"""
    number = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta(object):
        """docstring for Meta"""
        ordering = ('-created_date',)
        verbose_name='Заказ'
            

    def __str__(self):
        """
        String for representing the Model object
        """
        return "{}".format(self.number)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

    def get_all_products(self):
        return ', '.join([item.get_products() for item in self.items.all() ])

    def get_date(self):
        return self.created_date.strftime("%d.%m.%Y %H:%M")



        
class OrderItem(models.Model):
    """docstring for OrderItem"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=200, help_text='Product name')
    product_price = models.DecimalField(max_digits=4, decimal_places=0)
    amount = models.IntegerField()

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{}'.format(self.order)

    def get_cost(self):
        return self.product_price * self.amount

    def get_products(self):
        return '{}x{}'.format(self.product_name, self.amount)


