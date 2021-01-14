from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User

#USERAdminの定義をどのように変更すればいいのか
class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields =('user_id',)
class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomeUserAdmin(UserAdmin):
    model = User
    fieldsets =(
            ("ユーザー情報",{
                'fields':('user_id','password','email')}
            ),("権限",{
                'fields':('is_activate','is_staff')
            })
        )
    form = CustomeUserChangeForm
    add_form = CustomeUserCreationForm
    
    list_filter = ('is_activate','is_staff',)
    list_display =('user_id','email','is_activate','is_staff')
    search_fields = ['user_id',]
    ordering =('user_id',)

admin.site.register(User,CustomeUserAdmin)
# Register your models here.