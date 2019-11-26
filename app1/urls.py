from django.urls import path
from . import views
from django.conf.urls import url
from app1.views import ReportOrder, ReportOrderItem

urlpatterns = [
    url(r'^report-order/$', ReportOrder.as_view(), name='report-order'),
    url(r'^report-order-item/$', ReportOrderItem.as_view(), name='report-order-item'),

]