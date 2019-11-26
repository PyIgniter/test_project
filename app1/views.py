from django.shortcuts import render
from django.views.generic import View
from .models import Order, OrderItem
from django.db.models import Avg, Max, Min, Count

# Create your views here.

class ReportOrder(View):
    """docstring for ReportOrder"""
    def get(self, request):
        order = Order.objects.all()
        return render(request, 'app1/report_order.html', context={'order': order})


class ReportOrderItem(View):
    """docstring for ReportOrderItem"""
    def get(self, request):
        # колонки (имя товара, данные (Заказ {номер заказа} - Цена {цена товара в заказе} - Дата {дата покупки})
        data = []
        for i in OrderItem.objects.values('product_name').distinct():
            list_order = []
            for x in OrderItem.objects.filter(product_name=i['product_name']):
                t = "Заказ {} - Цена {} - Дата {}".format(str(x.order), str(x.product_price), str(x.order.created_date.strftime("%d.%m.%Y %H:%M"))) 
                list_order.append(t)
            list_order = str(list_order).strip("[]")
            i.update(data_order = list_order)
            data.append(i)
        # Самый покупаймый товар
        amount = OrderItem.objects.aggregate(Max('amount'))

        
        return render(request, 'app1/report_order_item.html', context={'data': data, 'amount': amount})