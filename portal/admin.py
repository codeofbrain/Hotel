from django.contrib import admin
from .models import Announcement,MaintenanceRequest,CustomUser,CleaningArea,CleaningDuty,AnnouncementComments
# Register your models here.

admin.site.register(Announcement)
admin.site.register(MaintenanceRequest)
admin.site.register(CustomUser)
admin.site.register(CleaningDuty)
admin.site.register(CleaningArea)
admin.site.register(AnnouncementComments)