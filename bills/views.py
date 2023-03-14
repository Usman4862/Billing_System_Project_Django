# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .forms import InfoForm
from .models import Customer, Product, Cust_bill, Inventory


# Create your views here.

def index(request):
    form = InfoForm(request.POST or None)

    username = request.POST.get('username')
    mobilenumber = request.POST.get('mobilenumber')
    email = request.POST.get('email')
    # username = form.cleaned_data.get("username")
    # mobilenumber = form.cleaned_data.get("mobilenumber")
    # email = form.cleaned_data.get("email")
    if form.is_valid():
        cus = Customer(customer_name=username,customer_mob_no=mobilenumber,customer_email=email)
        cus.save()
        print(form.cleaned_data)
    product = Product.objects.all()
    product_no = Product.objects.all().count()     
    print ("count: %d"% product_no)
    inventory = Inventory.objects.all()
    mylist = []
    # db store
    context = {
        'title': 'Myrel Billing System',
        'Name': username,
        'mobilenumber': mobilenumber,
        'products':product,
        'inventory':inventory,
        'product_no':product_no,
        'mylist':mylist
    }
    #print product

    # for p in product.product_set.all:
    #     print p.product.name

    if request.method == "POST" and username != None:
        return render(request, "bills/menu.html", context)

    return render(request, "bills/index.html", {'form': form, 'title': 'Billing System'})


def cal_amount(request):
    print("cal_amount")
    amount = 0
    count = 0

    username = request.POST.get('username')
    mobilenumber = request.POST.get('mobilenumber')

    products = Product.objects.all()
    total_count = Product.objects.all().count()
    for p in products:
        id = p.product_id
        q = request.POST.get('q_id_' + str(id))
        if q is not None and q != '' and int(q):
            q = int(q)
            amount += q * int(p.product_price)
            count += 1

    context = {
        'count': count,
        'amount': amount
    }
    # cus_name = request.POST.get('name')
    # x = request.POST.get('')
    # quantity2 = request.POST.get('quantity2')
    return render(request, "bills/bills.html", context)


def test_iterations(request):
    data = {
        "products":
            [


                     {
                         "name": "Aloo",
                           "price": 30
                      },


                        {
                            "name": "Gobhi",
                            "price": 40
                        }

            ]
    }

    return render(request=request, template_name="bills/test_iterations.html", context=data)
