from rest_framework.views import APIView


class FramgiaAPIView(APIView):

    response_data = dict(results={}, errors=[])

    def get_response_data(self, data):
        self.response_data['results'] = data

    def convert_querydict_to_dict(self, querydict):

        converted_dict = dict()
        for key, item in querydict.items():
            splited_item = item.split(',')
            if len(splited_item) == 1:
                converted_dict[key] = splited_item[0]
            else:
                converted_dict[key] = splited_item
        return converted_dict
