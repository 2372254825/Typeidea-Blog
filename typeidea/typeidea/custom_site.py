from django.contrib.admin import AdminSite

'''
把后台功按权限分开
'''
class CustomSite(AdminSite):
    site_header = 'Typekdea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')

