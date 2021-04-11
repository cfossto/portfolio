from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import VenueForm

# Create your views here.

def index(request,year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name,year)
    cal = HTMLCalendar().formatmonth(year,month)
    announcements = [
        {
            "date": "6-10-2020",
            "announcement":"Very good"
        },
        {
            "date": "12-13-2020",
            "announcement":"Yes indeed"
        }
    ]
    #return HttpResponse("<h1>%s</h1>" % title)
    return render(request,'events/calendar_base.html', { 'title':title,'cal':cal,'announcements':announcements}) # render out req to template, with template args
    

def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
    'events/add_venue.html',
    {
        'form':form,'submitted':submitted
    })