from django.shortcuts import render,get_object_or_404
from .models import CalendarEvent
from .forms import EntryForm
from django.http import HttpResponseRedirect
import datetime
import pytz
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/account/login/')
def show_calendar(request):
    calendarentries=CalendarEvent.objects.filter(eventdone=None)
    changetobeijing=datetime.timedelta(hours=8) #change to beijing time
    for cd in calendarentries:
        if datetime.datetime.now()>cd.remarkdate.replace(tzinfo=None)+changetobeijing:
            cd.tdelta=(datetime.datetime.now()-cd.remarkdate.replace(tzinfo=None)-changetobeijing).days
            cd.mark=True
        else:
            cd.tdelta=(cd.remarkdate.replace(tzinfo=None)+changetobeijing-datetime.datetime.now()).days
            cd.mark=False
    return render(request,"calendar/mycalendar.html",{'calendarentries':calendarentries})

def show_details(request,id):
    calendarentry=CalendarEvent.objects.filter(id=id)[0]
    return render(request,"calendar/details.html",{'calendarentry':calendarentry})

@login_required(login_url='/account/login/')
def add(request):
    if request.method=="POST":
        form=EntryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            remarkdate=form.cleaned_data['remarkdate']
            importance=form.cleaned_data['importance']
            descriptions=form.cleaned_data['descriptions']
            CalendarEvent.objects.create(
            name=name,
            remarkdate=remarkdate,
            descriptions=descriptions,
            importance=importance,
            ).save()
            return HttpResponseRedirect('/calendar/show-calendar/')
    else:
        form=EntryForm()
    return render(request,'calendar/form.html',{'form':form})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def delete(request,id):
    #entry_id=request.POST['id']
    try:
        entry=CalendarEvent.objects.get(id=id)
        entry.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def finish(request,id):
    try:
        entry=CalendarEvent.objects.get(id=id)
        entry.eventdone=True
        entry.save()
        return HttpResponse('1')
    except:
        return HttpResponse('2')

@login_required(login_url='/account/login/')
def todolish(request):
    calendarentries=CalendarEvent.objects.filter(eventdone=None)
    changetobeijing=datetime.timedelta(hours=8)
    for cd in calendarentries:
        if datetime.datetime.now()>cd.remarkdate.replace(tzinfo=None)+changetobeijing:
            cd.ispast=True
        else:
            cd.ispast=False
        cd.save()
    calendarentries_tdl=calendarentries.filter(ispast=False)
    for cd_tdl in calendarentries_tdl:
        cd_tdl.tdelta=(cd_tdl.remarkdate.replace(tzinfo=None)+changetobeijing-datetime.datetime.now()).days
    return render(request,"calendar/todolish.html",{'calendarentries_tdl':calendarentries_tdl})

def finished(request):
    finishedevents=CalendarEvent.objects.filter(eventdone=True)
    return render(request,"calendar/finished.html",{'finishedevents':finishedevents})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def deletefinished(request):
    id=request.POST['id']
    try:
        entry=CalendarEvent.objects.get(id=id)
        entry.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')
