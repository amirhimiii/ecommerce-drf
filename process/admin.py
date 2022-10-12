from django.contrib import admin
from .models import Cart, CartItem, Checkout


class CartInline(admin.StackedInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','status','ordered','date_paid']
    list_filter = ('user','status','ordered','date_paid')
    inlines = [CartInline,]



admin.site.register(Checkout)