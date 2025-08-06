# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(blank=True, null=True, default=timezone.now)
    role = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Team(models.Model):

    #__Team_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Team_FIELDS__END

    class Meta:
        verbose_name        = _("Team")
        verbose_name_plural = _("Team")


class Project(models.Model):

    #__Project_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_archive = models.BooleanField()
    slug = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Tool(models.Model):

    #__Tool_FIELDS__
    slug = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    category = models.TextField(max_length=255, null=True, blank=True)
    is_archive = models.BooleanField()

    #__Tool_FIELDS__END

    class Meta:
        verbose_name        = _("Tool")
        verbose_name_plural = _("Tool")


class Toolrunresult(models.Model):

    #__Toolrunresult_FIELDS__
    run_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)
    result_data = models.TextField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    execution_time = models.CharField(max_length=255, null=True, blank=True)
    source_platform = models.CharField(max_length=255, null=True, blank=True)
    score = models.CharField(max_length=255, null=True, blank=True)

    #__Toolrunresult_FIELDS__END

    class Meta:
        verbose_name        = _("Toolrunresult")
        verbose_name_plural = _("Toolrunresult")



#__MODELS__END
