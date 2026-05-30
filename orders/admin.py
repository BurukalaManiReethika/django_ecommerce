from django.contrib import admin

from .models import Order
from .models import OrderItem


class OrderItemInline(
    admin.TabularInline
):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'status',
        'paid',
        'created'
    )

    list_filter = (
        'status',
        'paid'
    )

    inlines = [
        OrderItemInline
    ]
