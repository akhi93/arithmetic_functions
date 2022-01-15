from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import re


# Create your models here.

# Models for the Arithmetic operations
class Operation(models.Model):
    name = models.CharField(max_length=100)
    formula = models.CharField(max_length=200)
    # Column to save all the variables in the formula
    parameters = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


# signal to extract and save variables present in the formula
@receiver(post_save, sender=Operation)
def update_parameters(sender, instance, **kwargs):
    # regex expression to extract variables present in the formula
    parameters = re.findall(r'\b[a-zA-Z]\b', instance.formula)
    instance.parameters = parameters
    Operation.objects.filter(id=instance.id).update(parameters=parameters)


post_save.connect(update_parameters, sender=Operation)
