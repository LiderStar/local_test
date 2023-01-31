from django import forms
from django.contrib.auth.models import User


from blog.models import Post


# from django
# Это форма не связана с моделью
class PostAdd(forms.Form):
    title = forms.CharField(max_length=256, label="Название", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Контент", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор", empty_label=None,
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    is_published = forms.BooleanField(initial=True)
    slug = forms.SlugField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


# Эта форма связана с моделью
class PostAddForm(forms.ModelForm):
    required_css_class = "required-field"

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'author', 'is_published', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'is_published': forms.NullBooleanSelect(),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
