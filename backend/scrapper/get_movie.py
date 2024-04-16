
from bs4 import BeautifulSoup
import requests
import json

def get_genre_cast(detail_link,movie_detail_dict):
    html_content = requests.get(f'https://paytm.com{detail_link}?tab=about')

    result = dict()
    movie_detail_dict['genre'] = ''
    movie_detail_dict['summary'] = 'sorry no summary provided'
    movie_detail_dict['casts'] = ''

    soup = BeautifulSoup(html_content.content, 'html.parser')

    try:
        div = soup.find('div',class_='MovieDetail_summary__uqUFy')
        summary = div.find('p').text.strip()
        movie_detail_dict['summary'] = summary
    except Exception:
        movie_detail_dict['summary'] = 'sorry no summary provided'

    div_tag = soup.find('div', class_='MovieDetail_movInfoCon__X4D6H')

    # Extract the genres
    try:
        if div_tag:
            genre_divs = div_tag.find_all('div', class_='MovieDetail_infoItem__xuA9M')  # Find all <div> tags within the main div
            for genre_div in genre_divs:
                genre_span = genre_div.find('span')  # Find the <span> tag within the <div>
                if genre_span and genre_span.text.strip() == "Genre":
                    genre_text = genre_div.text.strip().replace("Genre", "").strip()  # Get the text after removing "Genre" label
                    genres = [genre.strip() for genre in genre_text.split(",")]  # Split the text by comma and remove leading/trailing whitespace
                    movie_detail_dict['genre'] = genres[0]
                    break  # Break the loop after finding the genres
    except Exception:
        movie_detail_dict['genre'] = ''
    
    
    lead_cast_div = soup.find('div',class_='MovieDetail_leadCast__cdwZQ')
    casts = []
    try:
        for li in lead_cast_div.find_all('li'):
            actor = li.find('div',class_='MovieCast_celebName__aYi_z').text.strip()
            casts.append(actor)
        movie_detail_dict['casts'] = casts[0]
    except Exception:
        movie_detail_dict['casts'] = ''

def get_movies(place_name):
    place_endpoint = f'https://paytm.com/movies/{place_name}'
    response = requests.get(place_endpoint)

    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the unordered list with class "H5RunningMovies_gridWrapper__KuuvC"
    ul_tag = soup.find('ul', class_='H5RunningMovies_gridWrapper__KuuvC')

    movies = []

    # Find all list items within the unordered list
    if ul_tag:
        list_items = ul_tag.find_all('li')
        for li in list_items:

            # Find script tag within the list item
            script_tag = li.find('script', type='application/ld+json')

            link = li.find('a')['href']
    #         print(link)

            if script_tag:
                # Extract JSON-LD data from the script tag
                json_data = script_tag.string
                json_obj = json.loads(json_data)
                json_obj['movie_detail_link'] = link
                movies.append(json_obj)
    #             print("JSON-LD Data:", json_data)
    #             print()  # Add a blank line for separation
            # else:
            #     # print("Script tag not found within the list item.")
    # else:
    #     print("Unordered list with specified class not found.")
        
    for movie in movies:
        get_genre_cast(movie.get('movie_detail_link'),movie)
        
        try:
            rating = movie.get('aggregateRating').get('ratingValue')
        except Exception:
            rating = 7  ## hehe
        movie['rating'] = rating
        keys_to_remove = ['@context', '@type', 'releasedEvent','aggregateRating','url']
        for key in keys_to_remove:
            try:
                del movie[key]
            except Exception:
                pass

    return(movies)

