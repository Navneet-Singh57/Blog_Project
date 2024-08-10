from django import forms
from .models import PostModel, Comments

class PostModelForm(forms.ModelForm):
    contents = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = PostModel
        fields = ('title','contents')
        
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','contents')
        
class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here...'}))
    class Meta:
        model = Comments
        fields = ('content',)