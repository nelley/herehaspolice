from django import forms
from herehaspolice.models import ErrorReport


class Error_ReportForm(forms.ModelForm):
    
    class Meta:
        model = ErrorReport
        fields = ['errorContent']
        widgets = {
          'errorContent': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
