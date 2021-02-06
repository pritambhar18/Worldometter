from django.contrib.auth.models import User
import django_filters
from .models import reg_table
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = reg_table
        fields = ['aid', 'fname','location','branch','joiningdate']