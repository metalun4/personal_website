from django.contrib import admin

from website.models import ProfileInfo, ProfileSkill, SocialLinkInfo, SocialLink

admin.site.site_header = 'Website Administration'
admin.site.site_title = admin.site.index_title = 'Dashboard'


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


class ProfileSkillInline(admin.TabularInline):
    model = ProfileSkill
    extra = 1


class ProfileInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'author', 'profile_name', 'profile_image', 'location', 'bio', 'resume', 'show_email'
        ]})
    ]
    inlines = [SocialLinkInline, ProfileSkillInline]
    list_display = ['profile_name']
    search_fields = ['profile_name', 'bio']


# Register your models here.
admin.site.register(ProfileInfo, ProfileInfoAdmin)
admin.site.register(SocialLinkInfo)
