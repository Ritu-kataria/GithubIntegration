from django.contrib import admin
from .models import Issues

# Register your models here.
class IssuesAdmin(admin.ModelAdmin):
    readonly_fields=('issue_id',)
    list_display = [
        'issue_id', 'state', 'label', 'assignee', 'created_at', 'updated_at'
    ]
    search_fields = ('issue_id',)
    list_filter = ('issue_id', 'state', 'label', 'assignee', 'created_at')
    list_per_page = 20

admin.site.register(Issues, IssuesAdmin)