from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'college', views.CollegeSearchViewSet)
# router.register(r'branch', views.BranchSearchViewSet)
# router.register(r'city', views.CitySearchViewSet)
# router.register(r'advance', views.AdvanceSearchViewSet)

urlpatterns = [
    # url(r'^a', views.post_list),
    # url(r'^', include(router.urls)),
    url(r'^college', views.college_search),
    url(r'^branch', views.branch_search),
    url(r'^city', views.city_search),
    url(r'^', views.advance_search),

]
