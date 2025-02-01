from django.urls import path
from . import views

urlpatterns = [
    # path() maps a URL to a view function. The angle brackets are a Django convention indicating what part of the URL
    #   to extract as the variable value. The variable name is indicated in the angle brackets (here cve_id). So in the
    #   example of cve/CVE-2022-12222, "CVE-2022-12222" is assigned to cve_id and passed to the view.get_cve_info
    #   function.
    path('cve/<str:cve_id>', views.get_cve_info, name='get_cve_info'),
]