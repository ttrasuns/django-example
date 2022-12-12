from django.shortcuts import render, HttpResponse

# Create your views here.

def university(request):
    
    if request.method == "POST":
        full_name = request.POST["full_name"]
        mathematics = request.POST["mathematics_grade"]
        latvian_language = request.POST["latvian_language_grade"]
        foreign_language = request.POST["foreign_language_grade"]
        
        if int(mathematics) > 39 and int(latvian_language) > 39 and int(foreign_language) > 39:
            return HttpResponse(f"{full_name} can apply to university")
        else:
            return HttpResponse(f"{full_name} can not apply to university")
        
    return render(request,
                  template_name="university.html")
