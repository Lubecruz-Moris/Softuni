from django import forms

from online_library.web.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreationForm(ProfileBaseForm):
    pass

class ProfileEditForm(ProfileBaseForm):
    pass

class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookCreationForm(BookBaseForm):
    pass

class BookEditForm(BookBaseForm):
    pass
