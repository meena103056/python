from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

comments = []

def home(request):
    html = """
    <h1>Blog Comment System</h1>

    <form method="post" action="/comment/">
        Name: <input name="name"><br><br>
        Comment: <input name="comment"><br><br>
        <button>Submit Comment</button>
    </form>

    <hr>
    <h2>Comments</h2>
    """

    for i, c in enumerate(comments):
        status = "Approved" if c["approved"] else "Pending"

        html += f"""
        <p>
        <b>{c['name']}</b>: {c['comment']}
        <br>Status: {status}
        """

        if not c["approved"]:
            html += f' <a href="/approve/{i}/">Approve</a>'

        html += "</p><hr>"

    return HttpResponse(html)

def add_comment(request):
    if request.method == "POST":
        comments.append({
            "name": request.POST["name"],
            "comment": request.POST["comment"],
            "approved": False
        })
    return home(request)

def approve(request, id):
    comments[id]["approved"] = True
    return home(request)

urlpatterns = [
    path("", home),
    path("comment/", add_comment),
    path("approve/<int:id>/", approve)
]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py", "runserver", "0.0.0.0:8007"])