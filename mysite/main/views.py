from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import FileModel, descript
from .functs import file_to_text_to_result
from django.shortcuts import redirect
import json
# Create your views here.

def upload_files(response):
    return render(response, "main/upload.html")
   
def multiple_upload(request):
    files = request.FILES.getlist("files")
    request.session['count'] = len(files)
    files_list = []
    for file in files:
        files_list.append(FileModel(file=file))
    if files_list:
        FileModel.objects.bulk_create(files_list)
    return JsonResponse({'success':True}, status=200)

def description(request):
    if request.method == "POST":
        descName = request.POST.get('name')
        descText = request.POST.get('text')
        description = descript(text=descText, name=descName)
        description.save()
        return redirect('results')
    else:
        return render(request, "main/description.html")

def results(request):
    count = request.session.get('count')

    session_files = FileModel.objects.order_by('-uploaded_at')[:count]
    file_paths = []
    description = descript.objects.last()
    job_text = description.text if description.text else "No description provided"
    job_name = description.name if description.name else "No name provided"
    for file in session_files:
        file_paths.append(file.file.path)
    jsonfiles = file_to_text_to_result(file_paths, job_text, job_name)
    relevantcount = len(jsonfiles)

    filenames = []
    filerels = []
    filejsons = []
    for jsonfile in jsonfiles:
        # if jsonfile["Relevancy"] < 70:
        #   jsonfiles.remove(jsonfile)
        #   continue  

        name = jsonfile.pop("Name", None)
        relevancy = jsonfile.pop("Relevancy", None)
        if relevancy < 85:
            jsonfiles.remove(jsonfile)
            continue

        filenames.append(name)
        filerels.append(relevancy)
        filejsons.append(json.dumps(jsonfile, indent=4))

    relevantcount = len(jsonfiles)
    context = {
        'totalfiles': count, 
        'relevantfiles': relevantcount, 
        'file_data': list(zip(filenames, filerels, filejsons))
        }
    
    return render(request, "main/results.html", context)
    # return HttpResponse("debug")