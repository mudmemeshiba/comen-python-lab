#------------------------------------------- IMDB HEADER -------------------------------------------
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json
import time 

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"

### do not forget to uncomment the next line to read json data
data = read_json(filename)
### ----------------------------------------------------------
#------------------------------------------- IMDB HEADER -------------------------------------------

lenData = len(data)

def q1():
    ratingFord = []
    topFive = []
    for m in range(lenData):
        try:
            dirname = data[m]['director']['name']
            cast = data[m]['cast']
            rating = data[m]['ratingValue']
            if 'Steven Spielberg' not in dirname and dirname != None and cast != None:
                for a in cast:
                    actor = a.get('name')
                    if actor == 'Harrison Ford' and rating != '':
                        ratingFord.append([float(rating), dirname])
        except KeyError:
            pass

    sortedRating = sorted(ratingFord, reverse=True)
    count = 0
    for i in range(len(ratingFord)-1):
        if count > 4:
            break
        if sortedRating[i+1][0] < sortedRating[i][0]:
            count += 1
        topFive.append(sortedRating[i][1])

    for i in range(len(topFive)):
        print(sorted(topFive)[i])

def q2():
    moviesHT = []
    for m in range(lenData):
        try:
            dirname = data[m]['director']['name']
            rating = data[m]['ratingValue']
            cast = data[m].get('cast', [])
            if 'Steven Spielberg' not in dirname or 'George Lucas' not in dirname:
                # if any(a.get('name', '') == 'Harrison Ford' for a in m.get('cast', [])) and any(a.get('name', '') == 'Tommy Lee Jones' for a in m.get('cast', [])):
                if any(actor.get('name', '') == 'Harrison Ford' for actor in cast) and any(actor.get('name', '') == 'Tommy Lee Jones' for actor in cast):
                    moviesHT.append([float(rating), data[m]['name']])
        except KeyError:
            pass
    print(max(moviesHT)[1])

#--------------------------------------------------
# def q1():
#     ratingFord = []
#     for m in data:
#         if len(ratingFord) >= 9:
#             break
#         try:
#             dirname = m['director']['name']
#             cast = m['cast']
#             rating = m['ratingValue']
#             if 'Steven Spielberg' not in dirname and dirname != None and cast != None:
#                 for a in cast:
#                     actor = a.get('name')
#                     if actor == 'Harrison Ford' and rating != '':
#                         if float(m['ratingValue']) >= 8.0:
#                             ratingFord.append(dirname)
#         except KeyError:
#             pass
        
#     sortedRating = sorted(ratingFord)    
#     for i in sortedRating:
#         print(i)
    # dirName = [sortedRating[i][1]]
    # sortedDirName = sorted(dirName, reverse=False)

# def q1():
#     ratingFord = []
#     for m in data:
#         if len(ratingFord) >= 9:
#             break
#         try:
#             if 'Steven Spielberg' not in m['director']['name'] and m['director']['name'] != None and m['cast'] != None:
#                 for a in m['cast']:
#                     actor = a.get('name')
#                     if actor == 'Harrison Ford' and m['ratingValue'] != '':
#                         if float(m['ratingValue']) >= 8.0:
#                             ratingFord.append(m['director']['name'])
#         except KeyError:
#             pass
#     ratingFord = sorted(ratingFord)
#     for i in ratingFord:
#         print(i)

# def q2():
#     moviesHT = []
#     for m in data:
#         try:
#             dirname = m['director']['name']
#             rating = m['ratingValue']
#             if m['cast'] != None and m['name'] != None and ('Steven Spielberg' not in dirname or 'George Lucas' not in dirname):
#                 if (any(a.get('name', '') == 'Harrison Ford' for a in m.get('cast', []))) and (any(a.get('name', '') == 'Tommy Lee Jones' for a in m.get('cast', []))):
#                     moviesHT.append([rating, m['name']])
#         except KeyError:
#             pass
#     sortedMovie = sorted(moviesHT, reverse=True)
#     print(sortedMovie[0][1])
# ------------------------------------------------

# def q1():
#     directors = set()
#     rating_directors = []

#     for m in data:
#         director = m.get('director', {}).get('name')
#         cast = m.get('cast')
#         rating = m.get('ratingValue')

#         if director and cast:
#             if director != 'Steven Spielberg':
#                 for actor in cast:
#                     actor_name = actor.get('name')
#                     if actor_name == 'Harrison Ford' and rating:
#                         rating_directors.append((rating, director))
#                         break

#     rating_directors.sort(reverse=True, key=lambda x: float(x[0]))
#     top_directors = sorted(set(x[1] for x in rating_directors[:9]))
    
#     for director in top_directors:
#         print(director)

# def q2():
#     harrison_ford_movies = {}
    
#     for m in data:
#         director = m.get('director', {}).get('name')
#         cast = m.get('cast')
#         rating = m.get('ratingValue')

#         if director and cast:
#             if 'Steven Spielberg' not in director and 'George Lucas' not in director:
#                 actors = [actor.get('name') for actor in cast if actor.get('name') in ['Harrison Ford', 'Tommy Lee Jones']]
#                 if len(actors) == 2 and rating:
#                     harrison_ford_movies[m['name']] = float(rating)
    
#     if harrison_ford_movies:
#         max_movie = max(harrison_ford_movies, key=harrison_ford_movies.get)
#         print(max_movie)

#----- driver code
print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
    start = time.time()
    q1()
elif ans == '2':
    start = time.time()
    q2()
else:
    print('Nothing to do..')
end = time.time()
print(end-start)

    # for i in range(9):
    #     print(sortedDirName[i])
    
    # topFive = []
    # sortedRating = sorted(ratingFord, reverse=True)
    # count = 0
    # for i in range(9):
    #     if count > 4:
    #         break
    #     if sortedRating[i+1][0] < sortedRating[i][0]:
    #         count += 1
    #     topFive.append(sortedRating[i][1])
    # for i in range(9):
    #     print(sorted(topFive)[i])
