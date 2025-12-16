from rest_framework.decorators import api_view
from rest_framework.response import Response
from autohub.models import Cars, Sale, Rent, Transmission, Body, Brand
from .serializer import CarSerializer, SaleSerializer, RentSerializer, TransmissionSerializer, BrandSerializer, BodySerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def cars_list(request):
    cars = Cars.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(cars, request)
    serializer = CarSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def cars_create(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def cars_detail(request, pk):
    try:
        cars = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return Response('Обьэкт не найден!')
    
    if request.method == 'GET':
        serializer = CarSerializer(cars, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = CarSerializer(cars, request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

    if request.method == 'DELETE':
        cars.delete()
        return Response(status=204)
    





@api_view(['GET'])
def sale_list(request):
    sale = Sale.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(sale, request)
    serializer = SaleSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def sale_create(request):
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def sale_detail(request, pk):
    try:
        sale = Sale.objects.get(pk=pk)
    except Sale.DoesNotExist:
        return Response('Обьэкт не найден!')
    
    if request.method == 'GET':
        serializer = SaleSerializer(sale, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = SaleSerializer(sale, request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

    if request.method == 'DELETE':
        sale.delete()
        return Response(status=204)
    

@api_view(['GET'])
def rent_list(request):
    rent = Rent.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(rent, request)
    serializer = RentSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def rent_create(request):
    serializer = RentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def rent_detail(request, pk):
    try:
        rent = Rent.objects.get(pk=pk)
    except Rent.DoesNotExist:
        return Response('Обьэкт не найден!')
    
    if request.method == 'GET':
        serializer = RentSerializer(rent, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = RentSerializer(rent, request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

    if request.method == 'DELETE':
        rent.delete()
        return Response(status=204)
    

@api_view(['GET'])
def transmission_list(request):
    transmission = Transmission.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(transmission, request)
    serializer = TransmissionSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def transmission_create(request):
    serializer = TransmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def transmission_detail(request, pk):
    try:
        transmission = Transmission.objects.get(pk=pk)
    except Transmission.DoesNotExist:
        return Response('Обьэкт не найден!')
    
    if request.method == 'GET':
        serializer = TransmissionSerializer(transmission, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TransmissionSerializer(transmission, request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

    if request.method == 'DELETE':
        transmission.delete()
        return Response(status=204)
    

@api_view(['GET'])
def body_list(request):
    body = Body.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(body, request)
    serializer = BodySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def body_create(request):
    serializer = BodySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def body_detail(request, pk):
    try:
        body = Body.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return Response('Обьэкт не найден!')
    
    if request.method == 'GET':
        serializer = BodySerializer(body, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BodySerializer(body, request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

    if request.method == 'DELETE':
        body.delete()
        return Response(status=204)
    

@api_view(['GET'])
def brand_list(request):
    brand = Brand.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(brand, request)
    serializer = BrandSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def brand_create(request):
    serializer = BrandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def brand_detail(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response('Обьэкт не найден!')
    
    if request.method == 'GET':
        serializer = BrandSerializer(brand, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BrandSerializer(brand, request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

    if request.method == 'DELETE':
        brand.delete()
        return Response(status=204)
    

