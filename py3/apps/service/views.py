from rest_framework.response import Response
from py3.apps.service.appmodels.service_list import CategoryListAppModel, StoreListAppModel, ServiceListAppModel
from py3.apps.service.mappers.schemas import CategorySchema, ServiceSchema, StoreSchema
from py3.lib.rest_framework.custom_views import FramgiaAPIView
import ast


class CategoryListView(FramgiaAPIView):
    """
    get all categories or get store in a category
    """

    def get(self, request, category=None):
        """
        :param request(HTTPRequest):
        :param  category(String): A Category's name
        :return: all categories if category = None or all store in a category with name = category
        """
        search_query = self.convert_querydict_to_dict(request.QUERY_PARAMS)

        category_schema = CategorySchema()
        store_schema = StoreSchema()

        if category:
            search_query['category'] = category
            qs = CategoryListAppModel.get_store_list(category)
            results = []
            lst = []
            for tmp in qs:
                data, errors = store_schema.dumps(tmp[1])
                store = ast.literal_eval(data)
                data, errors = StoreSchema().load(store)
                lst += [errors]
                results += [store]
            self.get_response_data(results)
            self.response_data['errors'] = lst
            return Response(self.response_data)

        else:
            qs = CategoryListAppModel.get_store_list()
            data = [category_schema.dump(category) for category in qs]
            self.get_response_data(data)


            #validate data return
            for object in self.response_data['results']:
                data, errors = CategorySchema().load(object.data)
                self.response_data['errors'] += [errors]

            return Response(self.response_data)

        return Response(self.response_data)


class ServiceListView(FramgiaAPIView):

    """
        get all services information
    """
    def get(self, resquest):
        service_schema = ServiceSchema()
        qs = ServiceListAppModel.get_service_list()
        data = [service_schema.dump(service) for service in qs]
        self.get_response_data(data)

        for temp in self.response_data['results']:
            data, errors = ServiceSchema().load(temp.data)
            self.response_data['errors'] += [errors]
        return Response(self.response_data)
