from django.shortcuts import render
from apps.main.models import Product, Category, Order
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.decorators.cache import cache_page
from django.core.cache import cache

class MainListView(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        cache_category = cache.get('category')
        if not cache_category:
            category = Category.objects.all()
            cache.set('category', category, 60)
        else:
            category = cache_category
        product = Product.objects.all()
        context['category'] = category
        context['product'] = product

        return context
    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        cache_product = cache.get('category')
        if not cache_product:
            product = Product.objects.all()
            cache.set('product', product, 60)
        else:
            product = cache_product
        category = Category.objects.all()
        context['category'] = category
        context['product'] = product
        return context
    
# class LeoView(TemplateView):
#     template_name = 'result.html'

#     def get_context_data(self, **kwargs):
#         product = Product.objects.filter(id=id)
#         context = super(CartView, self).get_context_data(**kwargs)
#         context['product'] = product

def add_to_cart(request, id):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    print(cart_session)
    return HttpResponseRedirect('/')


def category(request, slug):
    category = Category.objects.get(slug=slug)
    product = Product.objects.filter(category = category)
    return render(request, 'category.html', {'product':product})

# class CategoryView(ListView):
#     model = Category
#     template_name = 'category.html'
#     def get_context_data(self, **kwargs):
#         context = super(CategoryView, self).get_context_data(**kwargs)
#         category = Category.objects.get(slug = self.kwargs('slug'))
#         product = Product.objects.filter(category = category)
#         context['product'] = product
#         context['category'] = category
#         return context

def leo(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'result.html', {'product':product})

# @login_required(login_url='signin')
def delete(request, id):
    cart_session = request.session.get('cart_session', [])
    remove_cart = cart_session
    remove_cart.remove(id)
    request.session['cart_session'] = remove_cart
    return HttpResponseRedirect('/cart')

def search(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        product_model = Product.objects.filter(title__contains = product)
        return render(request, 'search.html', {'product':product_model})

class ResultView(TemplateView):
    template_name = 'result.html'

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'

class CartView(TemplateView):
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart_session = self.request.session.get('cart_session', [])
        amount = len(cart_session)
        products = Product.objects.filter(id__in = cart_session)
        total_price = 0
        count = 0
        for i in products:
            i.count = cart_session.count(i.id)
            i.sum = i.count * i.price
            total_price += i.sum
        context['products'] = products
        context['amount'] = amount
        context['total_price'] = total_price
        return context

def table(request, id):
    if request.method == 'POST':
        order = Order.objects.get(id=id)
        cart_session = request.session.get('cart_session', [])
        amount = len(cart_session)
        order.phone = request.POST.get('phone')
        order.email = request.POST.get('email')
    # return HttpResponseRedirect('/')
    return render(request, 'cart.html', {'order':order})