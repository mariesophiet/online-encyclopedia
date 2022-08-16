from http.client import HTTPResponse
from django.shortcuts import render, redirect

from . import util

def index(request):
    print("index")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_title(request, title):
    print("title")
    return render(request, "encyclopedia/title.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def search(request):
    print("search")
    entries = util.list_entries()
    response = []
    q = request.GET["q"].lower()
    # check if there is actually a q variable in the http response
    if q:
        for entry in entries:
            # there exists an entry with the exact name of q
            if q == entry.lower():
                return redirect('encyclopedia:title', title=q)
            # add entry to list with entries that have q as a substring
            elif q.lower() in entry.lower():
                response.append(entry)
        # return the list of entries that match or return error message
        return render(request, "encyclopedia/search.html", {
                "entries": response
            })

def new(request):
    # if input post request
    if request.method == "POST":
        # check if the entry already exists
        heading = request.POST["title"]
        entries = util.list_entries()
        for entry in entries:
            if heading.lower() == entry.lower():
                # display error message and do not save file
                return render(request, "encyclopedia/new_page.html", {
                    "already_exists": True
                })
        # save file and show the new page 
        content = request.POST["markdown"]
        util.save_entry(heading, content)
        return redirect('encyclopedia:title', title=heading)

    # if input get request
    else:
        return render(request, "encyclopedia/new_page.html")

 
    