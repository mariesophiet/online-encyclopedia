from http.client import HTTPResponse
from django.shortcuts import render

from . import util

def index(request):
    print("index")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    print("title")
    return render(request, "encyclopedia/title.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def search(request):
    print("search")
    entries = util.list_entries()
    response = []
    q = request.GET["q"]
    # check if there is actually a q variable in the http response
    if q:
        for entry in entries:
            # there exists an entry with the exact name of q
            if q.lower() == entry.lower():
                return render(request, "encyclopedia/title.html", {
                    "entry": util.get_entry(q),
                    "title": q
                })
            # add entry to list with entries that have q as a substring
            elif q.lower() in entry.lower():
                response.append(entry)
        # check if there is anything in response. If yes, then print list 
        #if len(response) > 0:
        return render(request, "encyclopedia/search.html", {
                "entries": response
            })
    

 
    