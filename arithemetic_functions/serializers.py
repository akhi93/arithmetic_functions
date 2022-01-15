from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    Serializer,
    JSONField
)

from .models import Operation


# serializer for Operation Model
class OperationSerializer(ModelSerializer):
    class Meta:
        model = Operation
        fields = ('id', 'name', 'formula')


class PerformOperationSerializer(Serializer):
    operation_id = CharField(label="Id of function")
    # parameters will be passed as JSON object
    parameters = JSONField()

    def validate(self, attrs):
        operation_id = attrs.get('operation_id')
        parameters = attrs.get('parameters')
        # validate whether the operation object exists or not
        qs = Operation.objects.filter(id=operation_id)
        if not qs.exists():
            raise ValidationError("Operation does not exists")
        operation_obj = qs.first()
        # finding the missing parameter by using set operation
        missing_params = set(operation_obj.parameters) - set(list(parameters.keys()))
        if missing_params:
            raise ValidationError("Following parameters are missing:" + ",".join(
                list(missing_params)) + ". The given formula is " + operation_obj.formula)
        return attrs
