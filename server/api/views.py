from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .models import Person
from .serilizers import CartItemSerializer
from .models import Order
from .models import ItemModel
from django.core import serializers
from .helpers import OrderToShow


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_all(request):
    serializer = serializers.serialize('json', ItemModel.objects.all())
    print(serializer)
    return HttpResponse(serializer, content_type='application/json')

@csrf_exempt
def post(request):
    item = ItemModel()
    item.product_name = request.POST.get('name')
    item.product_price = request.POST.get('price')
    item.product_weight = request.POST.get('weight')
    ItemModel.save(item)
    print(len(ItemModel.objects.all()))
    return render(request, 'index.html')

@csrf_exempt
def postuser(request):
    item = Person()
    item.name = request.POST.get('name')
    item.surname = request.POST.get('price')
    item.citizenship = request.POST.get('weight')
    item.number = request.POST.get('weight')
    Person.save(item)
    print(len(ItemModel.objects.all()))
    return render(request, 'index.html')

@csrf_exempt
def postorder(request):
    item = Order()
    item.user_id = request.POST.get('user_id')
    item.item_id = request.POST.get('item_id')
    item.if_get = False
    Order.save(item)
    print(len(ItemModel.objects.all()))
    return render(request, 'index.html')

def get_not_recived_order(request):
    oreders = Order.objects.filter(if_get = False)
    l = []
    for i in oreders:
        l.append(OrderToShow(i.item_id, i.user_id))
    serializer = serializers.serialize('json', l)
    return HttpResponse(serializer, content_type='application/json')