from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User





class MagasAdminSite(AdminSite):
    site_title = "Magaságyás"
    site_header = "Magaságyás"


magasagyas_admin_site = MagasAdminSite()
magasagyas_admin_site.register(User,UserAdmin)
magasagyas_admin_site.register(Group,GroupAdmin)