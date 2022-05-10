from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Issues(models.Model):
    issue_id = models.IntegerField(_('Issue ID'), unique=True, db_index=True)
    title = models.CharField(_('Title'), max_length=255, null=True)
    number = models.IntegerField(_('Number'), null=True)
    label = models.CharField(_('Label'), null=True, max_length=255)
    assignee = models.CharField(_('Assignee'), null=True, max_length=120)
    state = models.CharField(_('State'),  max_length=255)
    created_at = models.DateTimeField(_('Created At'), help_text="Date when issue was created")
    updated_at = models.DateTimeField(_('Updated At'), help_text="Date when issue was modified", null=True)
    closed_at = models.DateTimeField(_('Closed At'), help_text="Date when issue was closed", null=True)

    class Meta:
        verbose_name = "Issue"
        verbose_name_plural = "Issues"

    def __str__(self):
        return str(self.issue_id)

