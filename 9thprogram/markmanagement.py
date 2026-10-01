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
            'NAME': 'students8.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

students = []


def get_grade(mark):

    mark = int(mark)

    if mark >= 90:
        return "A+"

    elif mark >= 80:
        return "A"

    elif mark >= 70:
        return "B"

    elif mark >= 60:
        return "C"

    elif mark >= 50:
        return "D"

    else:
        return "Fail"


def home(request):

    html = """
    <h1>Student Mark Management</h1>

    <form method="post" action="/add/">

        Name:
        <input name="name">
        <br><br>

        Roll Number:
        <input name="roll">
        <br><br>

        Course:
        <input name="course">
        <br><br>

        Mark:
        <input type="number" name="mark">
        <br><br>

        <button>
            Add Student
        </button>

    </form>

    <h2>Student Records</h2>
    """

    for i, student in enumerate(students):

        grade = get_grade(
            student["mark"]
        )

        html += f"""
        <p>

        <b>{student['name']}</b>

        - Roll No:
        {student['roll']}

        - Mark:
        {student['mark']}

        - Grade:
        {grade}

        <br>

        <a href="/detail/{i}/">
            View
        </a>

        |

        <a href="/delete/{i}/">
            Delete
        </a>

        </p>
        """

    return HttpResponse(html)


def add_student(request):

    if request.method == "POST":

        students.append({

            "name":
                request.POST.get("name"),

            "roll":
                request.POST.get("roll"),

            "course":
                request.POST.get("course"),

            "mark":
                request.POST.get("mark")

        })

    return home(request)


def detail(request, id):

    student = students[id]

    grade = get_grade(
        student["mark"]
    )

    return HttpResponse(f"""
        <h1>Student Result</h1>

        <p>
            Name:
            {student['name']}
        </p>

        <p>
            Roll Number:
            {student['roll']}
        </p>

        <p>
            Course:
            {student['course']}
        </p>

        <p>
            Mark:
            {student['mark']}
        </p>

        <p>
            Grade:
            <b>{grade}</b>
        </p>

        <a href="/">
            Back
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
        "program8.py",
        "runserver",
        "0.0.0.0:8003"
    ])