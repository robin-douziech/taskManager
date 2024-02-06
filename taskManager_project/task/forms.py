from django import forms
from . import models
from django.utils.safestring import mark_safe

class TaskForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['title'].required = True
		self.fields['title'].initial = ""

	def as_p(self):
		html_string = "<div class=\"form-container\">\n"
		for field in self :
			html_string += f"\t<div class=\"field-container\">\n"
			html_string += f"\t\t{field}\n"
			html_string += f"\t</div>\n"
		html_string += "</div>"
		return mark_safe(html_string)

	class Meta:
		model = models.Task
		exclude = []
		widgets = {
			'title': forms.TextInput(attrs={'placeholder': 'Titre de la tâche'}),
			'description': forms.Textarea(attrs={'placeholder': 'Description'}),
		}