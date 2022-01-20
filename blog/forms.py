from django import forms 
from blog.models import Comment

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  helper = FormHelper()
  helper.add_input(Submit('submit', 'Submit'))
  helper.form_method = 'POST'
