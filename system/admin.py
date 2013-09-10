from django.contrib import admin
from system.models import *


class DetailInfoInline(admin.StackedInline):
    	model = UserProfile
    	extra = 1

class MemberAdmin(admin.ModelAdmin):
        search_fields = ['nick_name']
    	inlines = [DetailInfoInline]

class EventAdmin(admin.ModelAdmin):
		list_filter = ['time']

admin.site.register(UserProfile, MemberAdmin)
admin.site.register(Event)
admin.site.register(EmailTemplete)