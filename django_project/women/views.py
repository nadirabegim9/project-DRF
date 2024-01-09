from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        return Response({'title': 'Гульнур Сатылганова'})



# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

