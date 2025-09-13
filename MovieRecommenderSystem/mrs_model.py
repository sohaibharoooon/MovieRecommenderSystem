#-----------------------------------Movie Recommender system-------------------------------------
import requests
import pickle
import pandas as pd

def fetch_poster(movie_id):
    #Fetch poster from API
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie): 
    #Fetch similar movies form trained model
    with open ('trained_model/Trained_Movies_Model.pkl', 'rb') as file:
        similarity=pickle.load(file)   
    movie_index= movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True, key= lambda x:x[1])[1:6]    
    recommended_movie=[]
    
    for i in movie_list:
        poster=[]        
        poster.append(movies.iloc[i[0]].title)
        try:
            poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
        except:
            poster.append("https://img.lazcdn.com/3rd/q/aHR0cHM6Ly9zdGF0aWMtMDEuZGFyYXoucGsvcC80Mzg0ZTFjNWE0YmNhZjlhMmJkMDYzMjJhNGJkZDU1ZS5qcGc=_200x200q75.png_.webp")
        recommended_movie.append(poster)        
    return recommended_movie


# Load movies dictionary
with open ('trained_model/movie_dict.pkl', 'rb') as file:
    movie=pickle.load(file)
movies=pd.DataFrame(movie)
def title():    
    movie_title=movies['title'].values
    return movie_title