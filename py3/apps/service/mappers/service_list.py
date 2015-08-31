from bpmappers import Mapper
from bpmappers.fields import (
    NonKeyDelegateField,
    RawField,
)


class ServiceMapperForServiceList(Mapper):
    service_id = RawField('id')
    service_name = RawField('name')


class ServiceCategoryMapperDorServiceList(Mapper):
    service_category = RawField('name')


class StoreMapperForServiceList(Mapper):
    store_name = RawField('name')


class ServiceListMapper(Mapper):

    service = NonKeyDelegateField(ServiceMapperForServiceList,
                                  attach_parent=True)
    service_category = NonKeyDelegateField(
        ServiceCategoryMapperDorServiceList,
        attach_parent=True
    )

    def filter_service(self):
        return self.data[0]

    def filter_service_category(self):
        return self.data[1]
