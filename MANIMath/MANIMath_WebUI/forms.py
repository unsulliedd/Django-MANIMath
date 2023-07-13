from django import forms
from django.utils.translation import gettext_lazy as _
from MANIMath_Data.models import *

class FunctionForm(forms.ModelForm):
    class Meta:
        model = FunctionModel
        fields = [
            'equation', 'equation_2', 'input_array',
            'x_range', 'y_range', 
            'x_length', 'y_length', 'domain', 
            'point_1', 'point_2',
            'iteration', 'text_color', 
            'equation_color', 'axes_color', 'line_color', 'shape_color',
            'scale', 'include_tip', 'include_numbers'
        ]

    def __init__(self, *args, **kwargs):
        show_equation2 = kwargs.pop('show_equation2', False)
        show_fields = kwargs.pop('show_fields', False)
        show_input = kwargs.pop('show_input', False)

        super().__init__(*args, **kwargs)

        if not show_fields:
            self.fields.pop('point_1')
            self.fields.pop('point_2')
            self.fields.pop('iteration')
        if not show_input:
            self.fields.pop('input_array')
        if not show_equation2:
            self.fields.pop('equation_2')

class RootFindingForm(forms.ModelForm):
    class Meta:
        model = RootFindingModel
        fields = [
            'equation',
            'x_range', 'y_range', 
            'x_length', 'y_length', 
            'point_1', 'point_2',
            'iteration', 'text_color', 
            'equation_color', 'axes_color', 'line_color', 'shape_color', 'tangent_color',
            'scale', 'include_tip', 'include_numbers'
        ]

class SortForm(forms.ModelForm):
    class Meta:
        model = SortModel
        fields = [
            'input_array',
            'target', 
            'text_color', 'line_color', 'shape_color',
            'scale',
        ]

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = [
            'input_array',
            'text_color', 'line_color', 'shape_color',
            'scale',
        ]