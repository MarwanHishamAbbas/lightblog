from django.contrib.auth.forms import UserCreationForm
from .models import User
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-field'
            visible.field.widget.attrs['required'] = True
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']