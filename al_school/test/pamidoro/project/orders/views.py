from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import SalesOrder
from .serializers import OrderSerializer


def index(request):
    context = {'orders': SalesOrder.objects.all()}
    return render(request, 'index.html', context)


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer