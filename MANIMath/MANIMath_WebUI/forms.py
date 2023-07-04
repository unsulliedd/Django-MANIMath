from django import forms
from django.utils.translation import gettext_lazy as _
from MANIMath_Data.models import *

class FunctionForm(forms.ModelForm):
    class Meta:
        model = FunctionModel
        fields = ['equation1','equation2']

class RootFindingForm(forms.ModelForm):
    class Meta:
        model = RootFindingModel
        fields = '__all__'

class SortForm(forms.ModelForm):
    class Meta:
        model = SortModel
        fields = '__all__'

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = '__all__'