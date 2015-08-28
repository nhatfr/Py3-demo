"""Service Viewの定義
"""


from rest_framework.views import APIView
from rest_framework.response import Response
from curama.apps.service.appmodels import ServiceListAppModel
from curama.apps.service.mappers import ServiceListMapper
from curama.lib.rest_framework.custom_paginator import (
    CuramaPageNumberPagination,
)
from curama.lib.rest_framework.custom_views import CuramaAPIView


class ServiceListView(CuramaAPIView):
    """サービス一覧を操作するAPIViewクラス
    """
    paginator = CuramaPageNumberPagination(page_size=1)

    def get(self, request, category=None, servicetype=None, postalcode=None, format=None):
        """サービス一覧を取得するAPI

        GETパラメータとURLパラメータを組み合わせて検索条件を表す辞書オブジェクトを
        作成し、ServiceListAppModelでqueryを取得します

        :param django-request-object request:
            getパラメータによりサービスの検索を実施します。
            サポートしているパラメーターは以下のとおりです

            :quantity:
                数量の絞り込み条件
                値は文字列で定義されています
            :feature:
                サービス特徴検索条件
                複数の値をとることもあります
        :param string category:
            urlから取得するパラメータ。カテゴリの検索条件として利用します
        :param string servicetype:
            urlから取得するパラメータ。サービスタイプの検索条件として利用します
        :param format:
            フォーマットの指定
        :rtype:
            rest_framework.response.Response
        :return:
            Responseオブジェクトを返却します
            オブジェクトを生成する際に辞書型へ変換されたself.response_dataを渡します
        """
        search_query = self.convert_querydict_to_dict(request.QUERY_PARAMS)

        # URLパラメータがある場合はsearch_queryに追加
        if category:
            search_query['category'] = category
        if servicetype:
            search_query['servicetype'] = servicetype
        if postalcode:
            search_query['postalcode'] = postalcode

        qs = ServiceListAppModel.get_service_list(search_query)
        pg = self.paginator.paginate_queryset(qs, request)
        data = [ServiceListMapper(service).as_dict() for service in pg]
        self.get_response_data(self.paginator.as_header_dict(), data)
        return Response(self.response_data)
