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

posts = []

def home(request):
    html = """
    <h1>Blog with Comments</h1>

    <form method="post" action="/add/">
        Title: <input name="title"><br><br>
        Content: <textarea name="content"></textarea><br><br>
        <button>Create Post</button>
    </form><hr>
    """

    for i, p in enumerate(posts):
        html += f"""
        <h2>{p['title']}</h2>
        <p>{p['content']}</p>

        <h4>Comments</h4>
        """

        for c in p["comments"]:
            html += f"<p>💬 {c}</p>"

        html += f"""
        <form method="post" action="/comment/{i}/">
            <input name="comment" placeholder="Write comment">
            <button>Add Comment</button>
        </form>
        <hr>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        posts.append({
            "title": request.POST["title"],
            "content": request.POST["content"],
            "comments": []
        })
    return home(request)

def comment(request, id):
    if request.method == "POST":
        posts[id]["comments"].append(request.POST["comment"])
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("comment/<int:id>/", comment)
]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py", "runserver", "0.0.0.0:8005"])