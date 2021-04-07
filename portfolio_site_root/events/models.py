from django.db import models

# Create your models here.



class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField("Zip", max_length=12)
    phone = models.CharField("Phone", max_length=20)
    web = models.URLField("Web address")
    email = models.EmailField("Email address")

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField("User Email")

    def __str__(self):
        return self.first_name + " " + self.last_name 



class Event(models.Model):
    name = models.CharField('Event Name',max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue,blank=True,null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    attendees = models.ManyToManyField(MyClubUser,blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



# A method with save-function
'''
from events.models import Event

event1 = Event(
    name = "Test event 1",
    event_date = "2020-01-28",
    venue = "Stadshallen",
    manager = "Roger"
)

event1.save()
'''

# Instantly creates a new DB-post
'''
Event.objects.create(
    name = "Xmas barbie",
    event_date = "2020-12-25",
    venue = "Noteareal Park",
    manager = "Santa"
)
'''

# READ one object
'''
Event.objects.get(id=1)
Event.objects.get(name="Xmas barbie")

osv..
'''

# Read multiple with filter()
'''
Event.objects.filter(manager="Roger", venue="Notareal Park")
osv..
'''

# Sorting - order_by

'''
Event.objects.order_by("thing")
'''

# It is possible to chain expressions.
# Slicing is how many posts you want
# Event.objects.all().order_by("event_date")[0] - first
# Event.objects.all().order_by("event_date")[3:15] - specific
# Event.objects.all().order_by("-event_date") - last (negative slicing no bueno)


## To Update many -> Filter the objects and then update the variables

# To DELETE -> Filter then delete. Event.objects.filter("thing").delete()