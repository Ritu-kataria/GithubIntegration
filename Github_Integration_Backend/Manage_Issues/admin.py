from django.contrib import admin
from .models import Issues, Labels, Assignees

# Register your models here.
class IssuesAdmin(admin.ModelAdmin):
    readonly_fields=('issue_id',)
    list_display = [
        'issue_id', 'state', 'created_at', 'updated_at'
    ]
    search_fields = ('issue_id',)
    list_filter = ('issue_id', 'state', 'created_at')
    list_per_page = 20

class LabelsAdmin(admin.ModelAdmin):
    readonly_fields=('label_id',)
    list_display = [
        'label_id', 'issue', 'name'
    ]
    search_fields = ('issue_id',)
    list_filter = ('issue_id', 'name')
    list_per_page = 20

class AssigneesAdmin(admin.ModelAdmin):
    readonly_fields=('assignee_id',)
    list_display = [
        'assignee_id', 'issue', 'name'
    ]
    search_fields = ('assignee_id',)
    list_filter = ('assignee_id', 'name')
    list_per_page = 20

admin.site.register(Issues, IssuesAdmin)
admin.site.register(Labels, LabelsAdmin)
admin.site.register(Assignees, AssigneesAdmin)