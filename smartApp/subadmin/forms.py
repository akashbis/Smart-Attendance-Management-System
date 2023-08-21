from django import forms  
from subadmin.models import Class  
class SubAdminForm(forms.ModelForm):  
    class Meta:  
        model = Class  
        fields = "__all__"  