from py3.apps.models import Store, Category, Service
from  rest_framework import viewsets, serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        field = ('name', 'description')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    index, new, show, update,modify, destroy category
    """
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    field = ('name', 'description')


# def get_service_list(category):
#     service_list = []
#     for store in  category.store_set.all():
#         for service in store.service_set.all():
#             service_list.append(service)
#     return service_list