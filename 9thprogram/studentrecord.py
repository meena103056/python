import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='student123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'students7.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

students = []


def home(request):

    html = """
    <h1>College Student Records</h1>

    <form method="post" action="/add/">

        Student Name:
        <input name="name">
        <br><br>

        Roll Number:
        <input name="roll">
        <br><br>

        Department:
        <select name="department">

            <option>
                Computer Science
            </option>

            <option>
                Computer Applications
            </option>

            <option>
                Information Technology
            </option>

        </select>

        <br><br>

        Year:
        <input name="year">

        <br><br>

        <button>
            Add Student
        </button>

    </form>

    <h2>Student List</h2>
    """

    for i, student in enumerate(students):

        html += f"""
        <p>

        <b>{student['name']}</b>

        <br>

        Roll No:
        {student['roll']}

        <br>

        Department:
        {student['department']}

        <br>

        Year:
        {student['year']}

        <br>

        <a href="/detail/{i}/">
            View Details
        </a>

        <a href="/delete/{i}/">
            Delete
        </a>

        </p>

        <hr>
        """

    return HttpResponse(html)


def add_student(request):

    if request.method == "POST":

        students.append({

            "name": request.POST.get("name"),

            "roll": request.POST.get("roll"),

            "department":
                request.POST.get(
                    "department"
                ),

            "year":
                request.POST.get("year")
        })

    return home(request)


def detail(request, id):

    student = students[id]

    return HttpResponse(f"""
        <h1>Student Information</h1>

        <h2>
            {student['name']}
        </h2>

        <p>
            Roll Number:
            {student['roll']}
        </p>

        <p>
            Department:
            {student['department']}
        </p>

        <p>
            Year:
            {student['year']}
        </p>

        <a href="/">
            Back to Home
        </a>
    """)


def delete_student(request, id):

    students.pop(id)

    return home(request)


urlpatterns = [

    path('', home),

    path('add/', add_student),

    path('detail/<int:id>/', detail),

    path('delete/<int:id>/', delete_student),

]


from django.core.management import execute_from_command_line

if __name__ == "__main__":

    execute_from_command_line([
        "program7.py",
        "runserver",
        "0.0.0.0:8004"
    ])