from rest_framework.response import Response

from rest_framework.views import APIView

from .models import *


class GetFoodInfoView(APIView):
    def get(self, request):
        querysetcategory = FoodCategory.objects.filter(food__is_publish=True).distinct()
        serializer_for_queryset_list = FoodListSerializer(
            instance=querysetcategory,
            many=True,
        )

        return Response(serializer_for_queryset_list.data)
