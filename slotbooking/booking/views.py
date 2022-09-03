from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account import utils
from booking.models import Space, Availability
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
            avails = Availability.objects.filter(date=date.date(), space_id = data['space_id'])
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


