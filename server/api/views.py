from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework import status
from .serilizers import CartItemSerializer
from .models import ItemModel

def get_all(request):
    serializer = CartItemSerializer(data=ItemModel.objects.all())
    if serializer.is_valid():
        serializer.save()
        return response.Response({'status':'success', 'data':serializer.data},
                             status = status.HTTP_200_OK)

@csrf_exempt
def post(request):
    item = ItemModel()
    item.product_name = request.POST.get('name')
    item.product_price = request.POST.get('price')
    item.product_weight = request.POST.get('weight')
    ItemModel.save(item)
    print(len(ItemModel.objects.all()))
    return render(request, 'index.html')