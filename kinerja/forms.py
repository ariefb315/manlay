from django import forms
from .models import Tr_header_skp, Ms_tugas_skp, Ms_Pegawai


class SKP(forms.ModelForm):
    class Meta:
        model = Tr_header_skp
        exclude = ()

class detil_SKP(forms.ModelForm):
    class Meta:
        model = Ms_tugas_skp
        exclude = ()
        localized_fields = ('__all__')