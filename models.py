# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Branch(models.Model):
    field_id = models.IntegerField(db_column='_id')  # Field renamed because it started with '_'.
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    fk_college_id = models.IntegerField(db_column='_college_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'branch'


class College(models.Model):
    field_id = models.IntegerField(db_column='_id')  # Field renamed because it started with '_'.
    college_code = models.CharField(max_length=255, blank=True, null=True)
    college_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'college'


class Cutoff(models.Model):
    field_id = models.IntegerField(db_column='_id')  # Field renamed because it started with '_'.
    cutoff_year = models.IntegerField(blank=True, null=True)
    round_no = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    fk_branch_id = models.IntegerField(db_column='_branch_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'cutoff'


class Stage(models.Model):
    field_id = models.IntegerField(db_column='_id')  # Field renamed because it started with '_'.
    mark = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    fk_cutoff_id = models.IntegerField(db_column='_cutoff_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'stage'
