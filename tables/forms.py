from django.forms import ModelForm
from authapp.models import WebUser
from django import forms

from tables.models import Facility


class ProfUserForm(ModelForm):
    class Meta:
        model = WebUser
        fields = ('avatar', 'last_name', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super(ProfUserForm, self).__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class FacilSelectWebuserForm(ModelForm):
    facility_name = forms.ModelChoiceField(label='Cклад', queryset=Facility.objects.all(), empty_label=None)

    class Meta:
        model = Facility
        fields = ['facility_name']

    def __init__(self, id, *args, **kwargs):
        super(FacilSelectWebuserForm, self).__init__(*args, **kwargs)
        self.fields['facility_name'].queryset = Facility.objects.filter(facility_id__in=id).order_by('facility_name')
        for field_name, field, in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            field.widget.attrs['onchange'] = 'form.submit();'
