from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account import utils
from booking.models import Space, Availability, Booking
from communication.models import Notification
import json
from datetime import datetime

def edit_slots(request,space_id):
    user = request.user
    if user.is_authenticated and user.type in["staff", "admin"]:
        space = Space.objects.get(id = space_id)
        context = {}
        context['space_name'] = space.name
        context['space_id'] = space.id
        context['sport_name'] = space.assoc_sport.sport_name
        # context['space_name'] = space.name

        if request.method == "POST":
            pass
        else:
            return render(request, "booking/add_slots.html", context)
    else:
        return utils.error1(request, "Only Staff accounts are allowed to edit slots for a space.")

@csrf_exempt
def get_slots(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            print(json.loads(request.body))
            data = json.loads(request.body)
            date = datetime.strptime(data['date'], "%d/%m/%Y")
            print(date.date())
            avails = Availability.objects.filter(date=date.date(), space_id = data['space_id']).order_by('slot__start_time')
            ret  = []
            for avail in avails:
                avail_obj = {}
                avail_obj['avail_id'] = avail.id
                avail_obj['slot_id'] = avail.slot.id
                avail_obj['slot_start_time'] = avail.slot.start_time.strftime("%-I:%M %p")
                avail_obj['slot_end_time'] = avail.slot.end_time.strftime("%-I:%M %p")
                avail_obj['units_available'] = avail.units_available
                avail_obj['total_units'] = avail.space.total_units
                ret.append(avail_obj)
            print(ret)
            return JsonResponse(ret, safe=False)

@csrf_exempt
def delete_slot(request):
    user = request.user
    if user.is_authenticated and user.type in ['staff']:
        if request.method == "POST":
            data = json.loads(request.body)
            avail_id = data['avail_id']
            cancel_reason = data['reason']
            availobj = Availability.objects.get(id=avail_id)
            availobj.delete()
            return HttpResponse()
    else:
        return utils.error1(request, "You need to be logged in as a staff account.")

@csrf_exempt
def add_slot(request):
    user = request.user
    if user.is_authenticated and user.type in ['staff']:
        pass
    else:
        return utils.error1(request, "You need to be logged in as a staff account.")

@csrf_exempt
def add_request(request):
    user = request.user
    if user.is_authenticated and user.type in ['student'] :
        data = json.loads(request.body)
        avail_id = data['avail_id']
        avail_obj = Availability.objects.get(id=avail_id)
        user_bookings = Booking.objects.filter(user=user)
        if(len(user_bookings) >= 3):
            return HttpResponse('OVER_BOOKED',status=101)
        elif avail_obj.units_available <= 0:
            return HttpResponse('FULL', status=102)
        elif user_bookings.filter(availability=avail_obj).exists():
            return HttpResponse('ALREADY_BOOKED', status = 104)
        b = Booking()
        b.user = user
        b.availability = Availability.objects.get(id=avail_id)
        b.approved = True
        b.availability.units_available = b.availability.units_available - 1
        b.save()
        n = Notification()
        n.for_user = user
        n.text = "Your request for space {avail_obj.space.name} in sport {avail_obj.space.assoc_sport.sport_name} from {avail_obj.slot.start_time} to {avail_obj.slot.end_time} on Date: {avail_obj.date} has been approved! Play hard :)"
        n.save()
        return HttpResponse()


def booking(request, space_id):
    user = request.user
    if user.is_authenticated and user.type in ['student']:
        if request.method == "POST":
            pass
        else:
            space = Space.objects.get(id = space_id)
            context = {}
            context['space_name'] = space.name
            context['space_id'] = space.id
            context['sport_name'] = space.assoc_sport.sport_name
            return render(request, "booking/booking.html", context)
    else:
        return utils.error1(request, "Only available for students.")