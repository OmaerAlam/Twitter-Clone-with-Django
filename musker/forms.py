from django import forms
from .models import Meep, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ---------------------------------------
# Profile Update Form
# ---------------------------------------
class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture", required=False)
    profile_bio = forms.CharField(
        label="Profile Bio",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profile Bio'}),
        required=False
    )
    homepage_link = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website Link'}),
        required=False
    )
    facebook_link = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook Link'}),
        required=False
    )
    instagram_link = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instagram Link'}),
        required=False
    )
    linkedin_link = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn Link'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'profile_bio',
            'homepage_link',
            'facebook_link',
            'instagram_link',
            'linkedin_link',
        )


# ---------------------------------------
# Meep Creation Form - Updated for modern UI
# ---------------------------------------
class MeepForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "What's happening?",
                "class": "form-control border-0 shadow-none",  # cleaner Twitter-style input
                "rows": 3,
                "style": "resize:none;"  # disables resizing
            }
        ),
        label="",  # No label, clean look
    )

    class Meta:
        model = Meep
        exclude = ("user", "likes",)


# ---------------------------------------
# User Registration Form
# ---------------------------------------
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Username field customization
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'User Name'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'
            '</span>'
        )

        # Password1 field customization
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Your password can’t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can’t be a commonly used password.</li>'
            '<li>Your password can’t be entirely numeric.</li>'
            '</ul>'
        )

        # Password2 field customization
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Enter the same password as before, for verification.</small>'
            '</span>'
        )
