from django.contrib import admin
from .models import Post, Category, Tag
from django.utils.html import format_html
from django.urls import reverse
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry


# Register your models here.
# '''
# 添加这个后打开分类页面后下方会出现文章页面
# '''
#
# class PostInline(admin.TabularInline):
#     fields = ('title', 'desc')
#     extra = 1
#     model = Post

@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    # # def save_model(self, request, obj, form, change):
    # #     obj.owner = request.user
    # #     return super(TagAdmin, self).save_model(request, obj, form, change)
    #
    # '''obj.owner固定名称，自动配置owner'''

# class CategoryOwnerFilter(admin.SimpleListFilter):
#     """
#     自定义过滤器只展示当前用户分类
#     """
#     '''
#     SimpleListFilter提供了两个属性和两个方法
#     '''
#     title = '分类过滤器'                 ''' title属性用于·展示标题 '''
#     parameter_name = 'owner_category'  ''' parameter_name 查询时URL参数的名字'''
#
#     def lookups(self, request, model_admin):
#         return Category.objects.filter(owner=request.user).values_list('id', 'name')
#
#     def queryset(self, request, queryset):
#         category_id = self.value()
#         if category_id:
#             return queryset.filter(category_id=self.value())
#         return queryset
#
    #list_filter = ['CategoryOwnerFilter']



@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = (
        'title', 'category', 'status',
        'created_time'
     )

    list_display_links = []
    #list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category_name']

    actions_on_top = True
    #actions_on_bottom = True

    exclude = ('owner',)
    #
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (

        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),

        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide', ),
            'fields': ('tag', ),
        })
    )
    #filter_horizontal = ('tag', )
    filter_vertical = ('tag', )


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/"
                    "4.0.0-beta.2/css/bootstrap.min.css", ),
        }
        js = ("https://cdn.bootcss.com/bootstrap/"
              "4.0.0-beta.2/js/bootstrap.bundle.js", )


    # def post_count(self, obj):
    #     return obj.post_set.count()

'''
 日志记录
'''
@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user',
                    'change_message'
                    ]

