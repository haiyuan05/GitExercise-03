from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel
# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get (self, request, *args, **kwargs):
        return render (request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs ):
        #every item from each category
        clothes = MenuItem.objects.filter(category__name__contains='clothes')
        shoes = MenuItem.objects.filter(category__name__contains='shoes')
        pants = MenuItem.objects.filter(category__name__contains='pants')
        watches = MenuItem.objects.filter(category__name__contains='watches')
        # pass into context
        context = {
            'clothes': clothes,
            'shoes': shoes,
            'pants': pants,
            'watches': watches,
        }
        #render template
        return render(request, 'customer/order.html', context)

def post(self, request, *args, **kwargs):
    order_items = {
        'items': []
    }
    items = request.POST.getlist('items[]')

    for item in items:
        menu_item= MenuItem.objects.get(pk__contains=int(item_))
        item_data - {
            'id': menu_item.pk,
            'name': menu_item.name,
            'price': menu_irem.price
        }

        order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items ['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add (*item_id)


        context = {
            'items': order_items ['items'],
            'price' : price
        }

        return render(request, 'customer/order_confirmation.html', context)

    


