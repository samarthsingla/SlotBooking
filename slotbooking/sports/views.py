from django.shortcuts import render
from booking.models import Space
from sports.models import Sport


def view_sport(request, sport_id):

    sport = Sport.objects.get(id = sport_id)
    spaces_set = sport.space_set.all()
    spaces = []
    print(spaces_set)
    count = 0
    for space in spaces_set:
        if space.available:
            count += 1
            spaces.append({'space_name':space.name, 'space_id':space.id, 'srno':count, 'total_units':space.total_units})
    print(spaces)
    return render(request, "sports/view_sport.html", {'sport_name':sport.sport_name, 'spaces':spaces})

def home(request):
    user = request.user
    if request.method == "GET":    
        sports = Sport.objects.all()
        return render(request, 'sports/homepage.html', {'sports': sports})


