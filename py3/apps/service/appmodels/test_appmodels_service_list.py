import pytest
from unittest.mock import patch, MagicMock


class TestServiceListAppModel(object):

    def _getTargetClass(self):
        from py3.apps.service.appmodels import ServiceListAppModel
        return ServiceListAppModel

    @patch('py3.apps.service.appmodels.ServiceListAppModel._filter')
    @patch('py3.apps.service.appmodels.ServiceListAppModel._get_queryset')
    def test_get_service_list(self, m1, m2):
        search_query_mock = {}
        cls = self._getTargetClass()
        result = cls.get_service_list(search_query_mock)
        assert m1.called
        assert m2.called

    def test__get_queryset(self):
        from sqlalchemy.orm.query import Query
        cls_ = self._getTargetClass()
        result = cls_._get_queryset()
        assert isinstance(result, Query)

    @pytest.mark.parametrize(
        'input, expected',
        [({}, None),
         ({'category': 'a'}, 'a')]
    )
    def test__filter_category(self, input, expected):
        from sqlalchemy.orm.query import Query
        from py3.apps.models import Category
        expected_obj = (Category.sa.name == expected)
        queryset = MagicMock(spec=Query)
        cls_ = self._getTargetClass()

        result = cls_._filter_category(queryset, **input)

        if not expected:
            assert queryset.filter.called is False
        else:
            call_arg = queryset.filter.call_args[0][0]
            assert str(call_arg) == str(expected_obj)
