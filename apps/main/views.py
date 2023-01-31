from django.shortcuts import render
from apps.main.models import Product, Category
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {'product':product, 'category':category})
def leo(request, id):
    product = Product.objects.get(id=id)
    # category = Category.objects.get(id=id)
    return render(request, 'result.html', {'product':product})
def add_to_cart(request, id):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    print(cart_session)
    return HttpResponseRedirect('/')
def delete(request, id):
    cart_session = request.session.get('cart_session', [])
    remove_cart = cart_session
    remove_cart.remove(id)
    request.session['cart_session'] = remove_cart
    return HttpResponseRedirect('/cart')
def cart(request):
    cart_session = request.session.get('cart_session', [])
    amount = len(cart_session)
    products = Product.objects.filter(id__in = cart_session)
    total_price = 0
    count = 0
    for i in products:
        i.count = cart_session.count(i.id)
        i.sum = i.count * i.price
        total_price += i.sum


    context = {'products':products, 'amount':amount, 'total_price':total_price}
    return render(request, 'cart.html', context)
