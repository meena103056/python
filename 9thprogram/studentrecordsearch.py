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
            'NAME': 'students5.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

students = []


def home(request):

    search = request.GET.get(
        "search",
        ""
    )

    html = """
    <h1>Student Record Management</h1>

    <form method="get">

        <input
            type="text"
            name="search"
            placeholder="Search Student"
        >

        <button type="submit">
            Search
        </button>

    </form>

    <br>

    <a href="/add/">
        Add Student
    </a>

    <h2>Student List</h2>
    """

    found = False

    for i, student in enumerate(students):

        if search.lower() in student[
            "name"
        ].lower():

            found = True

            html += f"""
            <p>

            <b>{student['name']}</b>

            - {student['course']}

            <a href="/detail/{i}/">
                View
            </a>

            <a href="/delete/{i}/">
                Delete
            </a>

            </p>
            """

    if not found:

        html += """
        <p>
            No student found.
        </p>
        """

    return HttpResponse(html)


def add_student(request):

    if request.method == "POST":

        students.append({

            "name": request.POST.get("name"),

            "age": request.POST.get("age"),

            "course": request.POST.get("course")

        })

        return home(request)

    return HttpResponse("""
        <h1>Add Student</h1>

        <form method="post">

            Name:
            <input name="name">
            <br><br>

            Age:
            <input name="age">
            <br><br>

            Course:
            <input name="course">
            <br><br>

            <button>
                Save
            </button>

        </form>
    """)


def detail(request, id):

    student = students[id]

    return HttpResponse(f"""
        <h1>Student Details</h1>

        Name: {student['name']}
        <br><br>

        Age: {student['age']}
        <br><br>

        Course: {student['course']}
        <br><br>

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
        "program5.py",
        "runserver",
        "0.0.0.0:8006"
    ])