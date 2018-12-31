from django.db import models

# Create your models here.


class CollegeResult(models.Model):
    id = models.IntegerField(primary_key=True)
    college_code = models.CharField(max_length=255, blank=True, null=True)
    college_name = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    cutoff_type = models.CharField(max_length=255, blank=True, null=True)
    stage_mark = models.IntegerField(blank=True, null=True)
    stage_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_college_result'
