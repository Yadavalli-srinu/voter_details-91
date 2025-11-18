from django.contrib import admin

from app1.models import voter_user_model,voter_profile_model
class voter_user_admin(admin.ModelAdmin):
    list_display=["name","voter_id"]
admin.site.register(voter_user_model,voter_user_admin)

class voter_profile_admin(admin.ModelAdmin):
    list_display=["name","date_birth","gender","mobile","aadhaar_number","address","city","state","pincode"]
admin.site.register(voter_profile_model,voter_profile_admin)

