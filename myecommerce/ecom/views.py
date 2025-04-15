from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from ecom.models import Coupon
from ecom.models import Product
from ecom.api.serializers import CouponSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class CouponAPIView(APIView):
    def get(self, request):
        coupons = Coupon.objects.all()
        serializer = CouponSerializer(coupons, many=True)
        return Response({"coupons":serializer.data})

class ProductViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]  # Token authentication
    #permission_classes = [IsAuthenticated]  # Only authenticated users can create products
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
