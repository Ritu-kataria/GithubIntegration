from operator import mod
from tkinter import CASCADE
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Issues(models.Model):
    issue_id = models.IntegerField(_('Issue ID'), unique=True, db_index=True)
    title = models.CharField(_('Title'), max_length=255, null=True)
    number = models.IntegerField(_('Number'), null=True)
    state = models.CharField(_('State'),  max_length=255)
    created_at = models.DateTimeField(_('Created At'), help_text="Date when issue was created")
    updated_at = models.DateTimeField(_('Updated At'), help_text="Date when issue was modified", null=True)
    closed_at = models.DateTimeField(_('Closed At'), help_text="Date when issue was closed", null=True)

    class Meta:
        verbose_name = "Issue"
        verbose_name_plural = "Issues"

    def __str__(self):
        return str(self.issue_id)

class Labels(models.Model):
    label_id = models.IntegerField(_('Label ID'), unique=True, db_index=True)
    issue = models.ForeignKey(Issues, related_name="issue_labels", null=True, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=255, null=True)
    description = models.CharField(_('Description'), max_length=300, null=True)

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"

    def __str__(self):
        return str(self.label_id)

class Assignees(models.Model):
    assignee_id = models.IntegerField(_('Assignee ID'), unique=True, db_index=True)
    issue = models.ForeignKey(Issues, related_name="issue_assignees", null=True, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=255, null=True)

    class Meta:
        verbose_name = "Assignee"
        verbose_name_plural = "Assignees"

    def __str__(self):
        return str(self.assignee_id)