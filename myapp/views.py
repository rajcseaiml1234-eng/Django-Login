from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "login.html", {"error": "Invalid Credentials"})

    return render(request, "login.html")


# DASHBOARD VIEW
@login_required
def dashboard(request):
    data = Student.objects.all()
    return render(request, "dashboard.html", {"data": data})


# ADD STUDENT
@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, "form.html", {"form": form, "title": "Add Student"})


# EDIT STUDENT
@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, "form.html", {"form": form, "title": "Edit Student"})


# DELETE STUDENT
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('dashboard')
    return render(request, "delete.html", {"student": student})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')