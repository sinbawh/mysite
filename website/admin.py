from django.contrib import admin
from website.models import Contact
from website.models import Newsletter
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ['name' , 'message']

admin.site.register(Newsletter)