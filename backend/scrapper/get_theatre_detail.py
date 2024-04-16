from bs4 import BeautifulSoup
import requests
from convert_to_sql_time import convert_to_sqlite_time

def get_theatre_details(place_name):
    
    theatre_links = []
    endpoint_for_theatre_name = f"https://paytm.com/movies/{place_name}/cinema-halls-and-movie-theatre"
    response_for_theatre_name = requests.get(endpoint_for_theatre_name)
    soup = BeautifulSoup(response_for_theatre_name.content, 'html.parser')

    # Extract information for each list item
    for li in soup.find_all('li', class_='CinemaListItem_cinemaListItemCon__JUOHu'):
        theatre_name= li.find('div', class_='CinemaListItem_itemDetail__xIIE7').h2.text.strip()
        theatre_showtime_link = li.find('div', class_='CinemaListItem_itemDetails__EVrkR').a['href']
        theatre_links.append("https://paytm.com"+theatre_showtime_link)
    
    
    def extract_time(s):
        if ':' in s:
            p = s.index(':')
            return convert_to_sqlite_time(s[p-2:p+6])
        else:
            None

    theatre_details_json = dict()

    for theatre_link in theatre_links:

        html_content = requests.get(theatre_link)
        soup = BeautifulSoup(html_content.content, 'html.parser')

        theatre_detail = soup.find('div',class_='CinemaDetailsV2_cinemaDetails__LO67d')
        theatre_name = theatre_detail.find('h2').text.strip()
        theatre_address = theatre_detail.find('p').text.strip()

        theatre_detail_dict = dict()
        showtime = dict()

        for li in soup.find_all('li',class_='MovieSessionsListing_movieSessions__lgEaM MovieSessionsListing_cdpSessions__QnM8W'):
            movie_name = li.find('div',class_='MovieSessionsListing_movieDetailsDivHeading__5ARu1').text.strip()
            time_schedule = []
            for l2 in li.find_all('li',class_='MovieSessionsListing_timeblock__S_Z44'):
                time = l2.find('div',class_='MovieSessionsListing_time__lMGDL').text.strip()
                extracted_time = extract_time(time)
                if extracted_time:
                    time_schedule.append(extracted_time)

            showtime[movie_name] = time_schedule
        theatre_detail_dict['showtimes'] = showtime
        theatre_detail_dict['address'] = theatre_address
        theatre_details_json[theatre_name] = theatre_detail_dict
    return theatre_details_json