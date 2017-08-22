from django.contrib import admin
from .models import Room, LiveRoom, History, AllSilent, OneSilent, ChatHistory, VisitHistory
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser, VertifyRegister, VertifyForgetpasswd


class UserCreationForm(forms.ModelForm):
    """A form for creating new users.
    Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('account', 'nickname', 'is_student')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('account', 'password', 'nickname',
                  'is_student', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('account', 'nickname', 'is_student', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('account', 'password')}),
        ('Personal info', {'fields': ('nickname', 'is_student')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account', 'nickname', 'is_student', 'password1', 'password2')}
         ),
    )
    search_fields = ('account',)
    ordering = ('account',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Room)
admin.site.register(LiveRoom)
admin.site.register(History)
admin.site.register(AllSilent)
admin.site.register(OneSilent)
admin.site.register(ChatHistory)
admin.site.register(VisitHistory)
admin.site.register(VertifyRegister)
admin.site.register(VertifyForgetpasswd)
# Register your models here.
