from django import forms
from app1.models import voter_user_model,voter_profile_model
class user_form2(forms.ModelForm):
    class Meta:
        model = voter_user_model
        fields='__all__' 

class profile_form2(forms.ModelForm):
    class Meta:
        model = voter_profile_model
        fields='__all__' 