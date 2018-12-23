from django.contrib.auth.models import User, Group
from rest_framework import serializers
from search.models import CollegeResult


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CollegeResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CollegeResult
        fields = ('college_name',
                  'cutoff_type',
                  'college_code',
                  'branch_name',
                  'cutoff_type',
                  'stage_mark',
                  'stage_rank',
                  )
