from django.core.management.base import BaseCommand, CommandError
from app1.models import Order, OrderItem
import datetime
import random

class Command(BaseCommand):

    help = 'Order generation'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Кількість згенерованих замовлень')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        #start  01.01.2018 09:00
        created_date = datetime.datetime(2018,1,1,9,00)
        for x in range(1,total+1):
            order = Order()
            order.number = x
            order.created_date = created_date + datetime.timedelta(hours=x)
            order.save()
            order_id = Order.objects.get(id=order.id)
            r = random.randint(2,6)
            for i in range(1,r):
                order_item = OrderItem()
                order_item.order = order_id 
                order_item.product_name = "Товар-{}".format(i)
                order_item.product_price = random.randint(100,999)
                order_item.amount = random.randint(1,10)
                order_item.save()

        self.stdout.write('Successfully created {} orders!'.format(total))

