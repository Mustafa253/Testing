from django.shortcuts import render
from .models import PythonType, Product, Review


# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getTypes(request):
    types_list=PythonType.objects.all()
    context={'types_list' : types_list }
    return render(request, 'pythonclubapp/types.html', context=context)

def getProducts(request):
    products_list=Product.objects.all()
    return render(request, 'pythonclubapp/products.html',{'products_list' : product_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    reviewcount=Review.objects.filter(product=id).count()
    reviews=Review.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'pythonclubapp/productdetails.html', context=context)


    
