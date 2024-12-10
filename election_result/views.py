from django.shortcuts import render, get_object_or_404,redirect
from .models import PollingUnit, AnnouncedPUResults,LGA
from django.http import HttpResponse

# Create your views here.

def polling_unit_results(request, uniqueid):
    polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)
    
    results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid=uniqueid)
    
    return render(request, 'polling_unit_results.html', {
        'polling_unit': polling_unit,
        'results': results,
    })


from django.shortcuts import render
from django.db.models import Sum
from .models import LGA, PollingUnit, AnnouncedPUResults

def lga_results(request):
    lgas = LGA.objects.filter(state_id=25)


    selected_lga_id = request.GET.get('lga_id')
    results = None
    total_scores = None

    if selected_lga_id:
        try:
           
            selected_lga_id = int(selected_lga_id)

            polling_units = PollingUnit.objects.filter(lga_id=selected_lga_id)
            polling_unit_ids = polling_units.values_list('uniqueid', flat=True)


            results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid__in=polling_unit_ids)

            total_scores = results.values('party_abbreviation').annotate(total_score=Sum('party_score'))
        except ValueError:
            selected_lga_id = None
    return render(request, 'lga_results.html', {
        'lgas': lgas,
        'results': results,
        'total_scores': total_scores,
        'selected_lga_id': selected_lga_id,
    })



def add_polling_unit_results(request):
    if request.method == "POST":

        polling_unit_id = request.POST.get('polling_unit_id')
        party_results = request.POST.getlist('party_result')

        polling_unit = PollingUnit.objects.create(
            uniqueid=polling_unit_id,
            polling_unit_id=polling_unit_id,
            ward_id=request.POST.get('ward_id'),
            lga_id=request.POST.get('lga_id'),
            state_id=25 
        )

        for party_result in party_results:
            party, score = party_result.split(':')
            AnnouncedPUResults.objects.create(
                polling_unit_uniqueid=polling_unit.uniqueid,
                party_abbreviation=party.strip(),
                party_score=int(score.strip())
            )
        return HttpResponse("Results added successfully!")

    return render(request, 'add_polling_unit_results.html')