from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q
from .forms import CreateStyleForms, UpdateStyleForms, searchForms, RequisitionForms
from .models import Styles, Requisition

# Create your views here.
def dashboard(request):
    return render(request, "app/dashboard.html")

# Show Styles
def styleShow(request):
    all_info = Styles.objects.all()
    context = {'records':all_info}
    return render(request, "app/styles.html", context=context)


# Create 
def createStyle(request):
    form = CreateStyleForms()
    if request.method == "POST":
        form = CreateStyleForms(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("styles")
    context = {'form':form}

    return render(request, "app/createRequisition.html", context=context) 

# Update 
def updateDetails(request, id):
    record = Styles.objects.get(id=id)
    form = UpdateStyleForms(instance=record)
    if request.method == "POST":
        form = UpdateStyleForms(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect("styles")
    context = {'form':form}
    return render(request, "app/updateDetails.html", context=context)


# Delete
def deleteSingleRecord(request, id):
    record = Styles.objects.get(id=id)
    record.delete()
    return redirect("styles")

# Show single record

def singleRecordDetails(request, id):
    records = Styles.objects.get(id=id)
    context = {'records':records}

    return render(request, "app/singleRecordDetails.html", context=context)


def styleShow(request):
    all_info = Styles.objects.all()
    if "search" in request.POST:
        query = request.POST.get('searchquery')
        all_info = Styles.objects.filter(
            Q(style_no__icontains=query) |
            Q(fabric_name__icontains=query)
        )
    context = {'records':all_info}
    return render(request, "app/styles.html", context=context)


def requisition(request):
    form = RequisitionForms()
    return render(request, "app/requisition.html",{"form": form})

def getStyleData(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax:
        style_id = request.GET.get('style_id')
        try:
            style = Styles.objects.get(id=style_id)
            data = {
                'style_no': style.style_no,
                'style_desc': style.style_desc,
                'fabric_name': style.fabric_name,
                'fabric_consumption': style.fabric_consumption,
                'fabric_cost': style.fabric_cost,
                'accessories_name': style.accessories_name,
                'accessories_consumption': style.accessories_consumption,
                'accessories_cost': style.accessories_cost,
                'wash_plant_name': style.wash_plant_name,
                'wash_cost': style.wash_cost,
            }
            return JsonResponse(data)
        except Styles.DoesNotExist:
            return JsonResponse({'error': 'Style not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)