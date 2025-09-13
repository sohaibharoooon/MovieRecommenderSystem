from django.shortcuts import render
from . import mrs_model as mrs


def mrs_model(request):
    # Default movie is Batman
    # This Function will be called when we click on Recommend button        
    selected_movie=request.POST.get("smovie","Batman")                        
    poster=mrs.recommend(selected_movie)
    movie_title=mrs.title()     
    param={"movie_title" : movie_title, "poster": poster, "selected_movie": selected_movie}
    return render (request,'mrs-model.html',param) 