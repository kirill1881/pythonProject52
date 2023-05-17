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
    serializer = serializers.serialize('json', Person.objects.all())
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
    item.surname = request.POST.get('surname')
    item.citizenship = request.POST.get('adres')
    item.number = request.POST.get('number')
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

def get_all_orders(request):
    oreders = Order.objects.all()
    serializer = serializers.serialize('json', oreders)
    return HttpResponse(serializer, content_type='application/json')

def get_not_recived_order(request):
    oreders = Order.objects.filter(if_get = False)
    serializer = serializers.serialize('json', oreders)
    return HttpResponse(serializer, content_type='application/json')



@csrf_exempt
def set_recived(request):
    id = request.POST.get('id')
    order = Order.objects.filter(id = id)[0]
    print(order)
    order.if_get = True
    Order.save(order)
    l = [order]
    serializer = serializers.serialize('json', l)
    return HttpResponse(serializer, content_type='application/json')

def get_user_by_id(request, pk):
    user = Person.objects.filter(id = pk)
    serializer = serializers.serialize('json', user)
    return HttpResponse(serializer, content_type='application/json')

def get_item_by_id(request, pk):
    user = ItemModel.objects.filter(id = pk)
    serializer = serializers.serialize('json', user)
    return HttpResponse(serializer, content_type='application/json')