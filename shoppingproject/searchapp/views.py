# from django.shortcuts import render
# from shoppingapp.models import Product
# from django.db.models import Q
# # Create your views here.
#
# def SearchResult(request):
#     products=None
#     query=None
#     if 'q' in request.GET:
#         query=request.GET.get('q')
#         products=Product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
#         return render(request,'search.html',{'query':query,'products':products})


from django.shortcuts import render
from shoppingapp.models import Product  # Ensure Product is imported correctly
from django.db.models import Q


def SearchResult(request):
    products = None
    query = None

    if 'q' in request.GET:  # Check if the 'q' parameter exists
        query = request.GET.get('q')  # Get the query string
        # Filter products based on name or description matching the query
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Render the results to the 'search.html' template
    return render(request, 'search.html', {'query': query, 'products': products})
