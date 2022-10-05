## views.py

# model = Cart

class Simple(APIView):
    def post(self,request):
        serializer = SerializerCart(data=request.data)
        serializer.is_valid = SerializerCart(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        cart = Cart.objects.all()
        serializer = SerializerCart(cart , many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs): # *args (none kwargs negah dare mishe)  **kwargs(kwargs negah dashte mishe) 
        model_id = kwargs.get('id', None)
        if not model_id:
            return JsonResponse({'error':'method /PUT/ not allowed'})
        
        try:
            instance = Cart.objects.get(id=model_id)
        except:
            return JsonResponse({"error":'objects does not exist'})

        serializer = SerializerCart(data=request.data , instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)




# serializer.py
class SerializerCart(serializers.Serializer):
    name = serializer.CharField()
    last_name = serializer.CharField()
    .
    .
    .

    def create(self, validate_data):
        return Cart.objects.create(**validate_data)

    def update(self, instance, validate_data):
        # baray gereftan va update kardan array ha
        return Cart.objects.filter(pk =instance.pk).update(**validate_data)
        # baray gerefta objects
        return Cart.objects.get(pk = instance.pk)

#__________________________________________________________