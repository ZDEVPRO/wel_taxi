from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required(login_url='/kirish/')
def index(request):
    orders_all = Order.objects.filter(status='yangi').order_by('-id')
    count = Order.objects.filter(status='yangi').count()

    context = {
        'orders': orders_all,
        'count': count
    }
    return render(request, 'driver/index.html', context)


@login_required(login_url='/kirish/')
def myorders(request):
    myorder = Order.objects.filter(driver=request.user).order_by('-id')

    context = {
        'myorder': myorder
    }
    return render(request, 'driver/myorders.html', context)


@login_required(login_url='/kirish/')
def order_detail(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        data = order
        data.status = 'olindi'
        data.driver = request.user
        data.save()
        return redirect('driver-order-detail', data.id)
    context = {
        'order': order
    }
    return render(request, 'driver/order_detail.html', context)


@login_required(login_url='/kirish/')
def success_order(request, id):
    order = Order.objects.get(id=id)
    arch = ArchiveOrder()
    arch.status = 'yetkazildi'
    arch.qayerdan = order.qayerdan
    arch.qayerga = order.qayerga
    arch.person_count = order.person_count
    arch.price = order.price
    arch.client_phone = order.client_phone
    arch.client_name = order.client_name
    arch.customer = order.customer
    arch.driver = order.driver
    arch.save()
    order.delete()
    return redirect('driver-myorders')


@login_required(login_url='/kirish/')
def client_in_car(request, id):
    order = Order.objects.get(id=id)
    order.client_in_car = 'Ha'
    order.save()
    return redirect('driver-order-detail', order.id)


@login_required(login_url='/kirish/')
def close_order(request, id):
    order = Order.objects.get(id=id)
    order.driver = None
    order.status = 'yangi'
    order.save()
    return redirect('driver')
