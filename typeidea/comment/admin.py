from django.contrib import admin
from .models import Comment
from typeidea.custom_site import custom_site
#from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content',  'created_time')
   # list_filter = ('target', 'nickname', 'content', 'website', 'created_time')
    #fields = ('target', 'nickname', 'content')

    #exclude = ('owner',)
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CommentAdmin, self).save_model(request, obj, form, change)
