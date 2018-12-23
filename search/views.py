from rest_framework import generics, permissions, status, filters

# Create your views here.


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.settings import api_settings

from search.models import CollegeResult
from search.permissions import ReadOnly
from search.serializers import CollegeResultSerializer


class CollegeSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = CollegeResult.objects.all()
    serializer_class = CollegeResultSerializer
    permission_classes = (ReadOnly,)  # (permissions.IsAuthenticatedOrReadOnly, ReadOnly,)


class CitySearchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed.
    """
    queryset = CollegeResult.objects.all()
    serializer_class = CollegeResultSerializer
    # permission_classes = (ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('cutoff_type')


class BranchSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CollegeResult.objects.all()
    serializer_class = CollegeResultSerializer
    permission_classes = (ReadOnly,)


class AdvanceSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CollegeResult.objects.all()
    serializer_class = CollegeResultSerializer
    permission_classes = (ReadOnly,)


@api_view(["GET"])
def college_search(request):
    if request.method == 'GET':

        # Handle Request Params
        college_id = request.query_params.get('id', None)

        # Query DB
        queryset = CollegeResult.objects.all()
        if college_id is not None:
            queryset = queryset.filter(college_code=college_id)

        # Apply Pagination
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = CollegeResultSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def branch_search(request):
    if request.method == 'GET':

        # Handle Request Params
        name = request.query_params.get('name', None)
        code = request.query_params.get('code', None)

        # Query DB
        queryset = CollegeResult.objects.all()
        if name is not None:
            queryset = queryset.filter(branch_name__icontains=name)
        if code is not None:
            queryset = queryset.filter(branch_code__icontains=id)

        # Apply Pagination
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = CollegeResultSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def city_search(request):
    if request.method == 'GET':

        # Handle Request Params
        name = request.query_params.get('name', None)

        # Query DB
        queryset = CollegeResult.objects.all()
        if name is not None:
            queryset = queryset.filter(city__icontains=name)

        # Apply Pagination
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = CollegeResultSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def advance_search(request):
    if request.method == 'GET':

        # Handle Request Params
        mark = request.query_params.get('mark', None)
        city = request.query_params.get('city', None)
        branch_name = request.query_params.get('branch', None)
        college_name = request.query_params.get('college', None)

        # Query DB
        queryset = CollegeResult.objects.all()
        if mark is not None:
            queryset = queryset.filter(stage_mark__lte=mark)
        if city is not None:
            queryset = queryset.filter(city__icontains=city)
        if branch_name is not None:
            queryset = queryset.filter(branch_name__icontains=branch_name)
        if college_name is not None:
            queryset = queryset.filter(college_name__icontains=college_name)

        # Apply Pagination
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = CollegeResultSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
