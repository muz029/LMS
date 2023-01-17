from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Students


def index1(request):
    mystudents = Students.objects.all().values()
    output = ""
    datarow = ""
    for std in mystudents:
        datarow += std["StudentId"] + std["StudentName"] + std["Gender"] + std["Year"] + std["ClassId"] + "/n"
        output += datarow
    return HttpResponse(output)


def index(request):
    mymembers = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('addstudent.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    studentid = request.POST['StudentId']
    studentname = request.POST['StudentName']
    gender = request.POST['Gender']
    year = request.POST['Year']
    classid = request.POST['Class']
    std = Students(StudentId=studentid, StudentName=studentname, Gender=gender, Year=year, ClassId=classid)
    std.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    std = Students.objects.get(StudentId=id)
    std.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = Students.objects.get(StudentId=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    studentid = request.POST['StudentId']
    studentname = request.POST['StudentName']
    gender = request.POST['Gender']
    year = request.POST['Year']
    classid = request.POST['ClassId']

    student = Students.objects.get(StudentId=id)
    student.StudentId = studentid
    student.StudentName = studentname
    student.Gender = gender
    student.Year = year
    student.ClassId = classid

    student.save()
    return HttpResponseRedirect(reverse('index'))


def testing(request):
    mymembers = Students.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'Student_Name': mymembers,
    }
    return HttpResponse(template.render(context, request))
