from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

# -----------------------------------------
# Unregister Group (optional for simplification)
# -----------------------------------------
admin.site.unregister(Group)

# -----------------------------------------
# Inline Profile with User in Admin
# -----------------------------------------
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False  # Prevent accidental deletion
    verbose_name_plural = 'Profile'
    fk_name = 'user'  # Assumes Profile has a OneToOneField to User

# -----------------------------------------
# Customize User Admin
# -----------------------------------------
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]  # Display only the username
    inlines = [ProfileInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

# -----------------------------------------
# Unregister and Re-register User with Profile Inline
# -----------------------------------------
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# -----------------------------------------
# Register Meep model in Admin
# -----------------------------------------
admin.site.register(Meep)
