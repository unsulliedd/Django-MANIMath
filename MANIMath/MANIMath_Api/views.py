from rest_framework.response import Response
from rest_framework import viewsets
from MANIMath_Api.serializers import *

class ModelViewSet(viewsets.ViewSet):
    def list(self, request):
        user = request.user
        function_models = FunctionModel.objects.filter(user=user)
        root_finding_models = RootFindingModel.objects.filter(user=user)
        sort_models = SortModel.objects.filter(user=user)
        search_models = SearchModel.objects.filter(user=user)

        function_serializer = FunctionModelSerializer(function_models, many=True)
        root_finding_serializer = RootFindingModelSerializer(root_finding_models, many=True)
        sort_serializer = SortModelSerializer(sort_models, many=True)
        search_serializer = SearchModelSerializer(search_models, many=True)

        return Response({
            'function_models': function_serializer.data,
            'root_finding_models': root_finding_serializer.data,
            'sort_models': sort_serializer.data,
            'search_models': search_serializer.data
        })

