from django import forms

from gamesplay_app.web.models import Profile, Game


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreationForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
