# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

def index(request):
    in_progress = progress.objects.filter(completed=False).order_by('-updated')
    in_progress = in_progress[:min(5,len(in_progress))]
    for i in range(len(in_progress)):
        in_progress[i] = complaint.objects.get(id=in_progress[i].id)
    future = complaint.objects.filter(assign=None).order_by('created')
    future = future[:min(5,len(future))]
    recent = complaint.objects.filter().order_y

