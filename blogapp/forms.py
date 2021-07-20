from.models import blog
from django import forms

class f(forms.ModelForm):
    class meta :
        model=blog
        fields = ['blog_id','blogname','desc','image']
