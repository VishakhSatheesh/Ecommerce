from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Product, Order
from .serializers import *
from .utils import is_admin
from rest_framework.permissions import AllowAny
class RegisterView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"})
        return Response(serializer.errors)

class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)

    def post(self, request):
        if not is_admin(request.user):
            return Response(
                {"error": "Only admins can add products"},
                status=403
            )

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      
        
class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if is_admin(request.user):
            orders = Order.objects.all()
        else:
            orders = Order.objects.filter(customer=request.user)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class OrderStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_id):
        if not is_admin(request.user):
            return Response(
                {"error": "Only admins can update orders"},
                status=403
            )

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        order.status = request.data.get('status', order.status)
        order.save()

        return Response({"message": "Order status updated"})
