from django.forms import ModelForm

from WebExam2.Notes.models import Profile, Note


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


# class DeleteProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance
