from py3.apps.models import (
    Category,
    Service,
    Store,
)


class ServiceListAppModel(object):

    @classmethod
    def get_service_list(cls, search_query):
        queryset = cls._get_queryset()
        queryset = cls._filter(queryset, search_query)
        return queryset

    @classmethod
    def _get_queryset(cls):
        service_list_qs = Service.sa.query(
            Service.sa,
            Category.sa,
        ).distinct()
        return service_list_qs

    @classmethod
    def _filter(cls, queryset, search_query):
        run_cls_method = [attr for attr in dir(cls) if '_filter_' in attr]
        for method in run_cls_method:
            queryset = getattr(cls, method)(queryset, **search_query)
        return queryset

    @classmethod
    def _filter_category(cls, queryset, category=None, **kwargs):
        if not category:
            return queryset
        return queryset.filter(Category.sa.name == category)


class CategoryListAppModel(object):

    @classmethod
    def get_store_list(cls, category=None):
        if category:
            return Store.sa.query(Category.sa, Store.sa).filter(Category.sa.name == category).distinct()
        return Category.sa.query(Category.sa).distinct()

# class StoreListAppModel(object):
#
#     @classmethod
#     def get_store_list(cls, search_query):
#         queryset = cls._get_queryset()
#         queryset = cls._filter(queryset, search_query)
#         return queryset
#
#     @classmethod
#     def _get_queryset(cls):
#         store_list_qa = Category.sa.query(Store.sa)
#         return store_list_qa
#
#     @classmethod
#     def _filter(cls, queryset, search_query):
#         run_cls_method = [attr for attr in dir(cls) if '_filter_' in attr]
#         for method in run_cls_method:
#             queryset = getattr(cls, method)(queryset, **search_query)
#         return queryset
