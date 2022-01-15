from django.urls import path

from .views import OperationCreateAPIView, OperationListAPIView, OperationRetrieveUpdateDestroyAPIView, \
    PerformOperationAPIView

urlpatterns = [
    # API url for add operation
    path('add-operation/', OperationCreateAPIView.as_view(), name='add-operation'),
    # API url for retrieve/update/delete operation
    path('<int:pk>/retrieve-update-delete/', OperationRetrieveUpdateDestroyAPIView.as_view(),
         name='etrieve-update-delete'),
    # API url to get all the saved operations
    path('get-all-operations/', OperationListAPIView.as_view(), name='gell-all-operations'),
    # API url to execute operation
    path('perform-operations/', PerformOperationAPIView.as_view(), name='perform-operations'),

]
