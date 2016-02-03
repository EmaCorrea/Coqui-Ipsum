from django import forms
from .models import Word

class ChooseForm(forms.ModelForm):
	class Meta:
		model = Word
		fields = ('paragraph','type','start')

"""erase this eventually