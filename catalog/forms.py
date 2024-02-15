from django import forms

from catalog.models import Product, Blog, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Слово "{word}" запрещено к использованию!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Слово "{word}" запрещено к использованию!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('product', 'version_number', 'name', 'is_active')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Слово "{word}" запрещено к использованию!')
        return cleaned_data


class BlogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('name', 'content', 'image', 'is_published',)