from django.shortcuts import render
from web.models import SavorTeam, Position

def index(request):
    pos_lists = Position.objects.filter(is_active=True).order_by("-id")
    team_lists = SavorTeam.objects.filter(is_active=True).order_by("-id")
    return render(request, "web/index.html", locals())


def join_submit(request):
    return render(request, "web/index.html", locals())
