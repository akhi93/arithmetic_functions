from django.shortcuts import render
import math
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import OperationSerializer, PerformOperationSerializer
from .models import Operation


# APIView to create all the operations
class OperationCreateAPIView(CreateAPIView):
    """
    :parameter
    -name :  name of the operation
    -formula : formula of operation
                ex: for addition "x+y"
                  : for factorial math.factorial(n)
    """
    serializer_class = OperationSerializer
    permission_classes = [AllowAny]
    queryset = Operation.objects.all()


# APIView for List all the operations
class OperationListAPIView(ListAPIView):
    serializer_class = OperationSerializer
    permission_classes = [AllowAny]
    queryset = Operation.objects.all()


# APIView for retrieve/update/delete all the operations
class OperationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OperationSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    queryset = Operation.objects.all()


# APIView for perform operations

class PerformOperationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args: operation_id - Id of an operation
        parameters : Parameters of an equation(In json format-Values should be either int or float)
        :param kwargs:
        :return:Result of an operation
        """
        data = request.data
        serializer = PerformOperationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # get operation id and parameters from serializer
            operation_id = data.get('operation_id')
            parameters = data.get('parameters')
            operation_obj = Operation.objects.get(id=operation_id)
            # Parse and assign each parameter from parameter dictionary
            for k, v in parameters.items(): exec(k + '=(v)')
            formula = operation_obj.formula
            # execute formula(type:str) saved in model using eval function
            try:
                result = eval(formula)
            except ZeroDivisionError:
                return Response({"error" :"Division by zero cannot be possible"}, status=HTTP_400_BAD_REQUEST)
            if isinstance(result, float):
                result = float("{:.2f}".format(result))
            return Response({"result":result}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
