from django.shortcuts import render
from .models import Course,Enrollment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    return render(request, "home.html")

def course_list(request):
    courses = Course.objects.all()

    paginator = Paginator(courses, 3)  # 3 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "course_list.html", {"page_obj": page_obj})

def course_detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, "course_detail.html", {"course": course})

@login_required
def enroll(request, id):
    course = Course.objects.get(id=id)

    # Prevent duplicate enrollment
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        Enrollment.objects.create(
            user=request.user,
            course=course
        )

    return render(request, "enroll_success.html", {"course": course})

@login_required
def dashboard(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"enrollments": enrollments})

