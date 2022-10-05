
# class AddProductToCart(APIView):
#     serializer_class = CartSerializers
#     queryset = CartItem.objects.all()

#     def get_queryset(self, pk):
#         product =  get_object_or_404(Product, pk=pk)
#         try:
#             order = Cart.objects.get(user=request.user, ordered=True)
#         except ObjectDoesNotExist:
#             order = Cart.objects.create(user=request.user, status='NP', ordered=True, date_paid=timezone.now())
#         order = Cart.objects.filter(user=request.user).first()
    
#         cart_item_created, cart_item  = CartItem.objects.get_or_create(product=product , order=order )
#         if cart_item_created:
#             cart_item_created.quantity += 1
#             cart_item_created.save()
#             messages.success(request,f'<< {product.title} >> add to cart')
#             # return redirect('order-summary')
#         messages.success(request,f'{product.title} add to cart')
#         # return redirect('product-list')

# add_to_product = AddProductToCart.as_view()



# class RemoveFromCart(APIView):
#     serializer_class = CartItemSerializers

    
#     def get_queryset(self,pk):
#         cart_item= get_object_or_404(CartItem, order__user=request.user, product__pk=pk)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#             messages.warning(request,f'one order of << {cart_item.product.title} >> deleted ')
#             # return redirect('order-summary')
#         else:
#             messages.warning(request,'delete from cart')
#             messages.warning(request,f'<< {cart_item.product.title} >>delete from cart')
#             cart_item.delete()
#             # return redirect('product-list')
#     def get(self, request):    
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset =CartItem.objects.all()
#         serializer = CartItemSerializers(queryset, many=True)
#         return Response(serializer.data)   
    
#     def create(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset =CartItem.objects.all()
#         serializer = CartItemSerializers(queryset)
#         return Response(serializer.data)



