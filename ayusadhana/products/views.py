from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator
# Create your views here.


@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        try:
            products = Products.objects.all()
            page = request.GET.get('page', 1)
            page_size = 30

            paginator = Paginator(products, page_size)
            total_pages = paginator.num_pages

            serializer = ProductSerializer(paginator.page(page), many=True)
            return JsonResponse({"Page_Count": total_pages, "Products": serializer.data},
                                status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return Response({
                "status": False,
                "message": "Invalid Page Number"
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):

    try:
        product = Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pass





