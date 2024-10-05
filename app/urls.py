from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", styleShow, name="styles"),
    path("createStyle/", createStyle, name="createStyle"),
    path("updateDetails/<int:id>", updateDetails, name="updateDetails"),
    path("singleDetails/<int:id>", singleRecordDetails, name="singleDetails"),
    path("deleteSingleRecord/<int:id>", deleteSingleRecord, name="deleteSingleRecord"),
    path("search/", searchForms, name="search"),
    path("requisition/",requisition, name="requisition"),
    path("getStyleData/", getStyleData, name="getStyleData"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
