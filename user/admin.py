from django.contrib import admin
from .models import Profile, User
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    def __str__(self):
        return self.user.username

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'password']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(Profile)
admin.site.register(User, UserAdmin)