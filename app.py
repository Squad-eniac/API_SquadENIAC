from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route('/')
def get_list_characters_page():
    url = 'https://rickandmortyapi.com/api/character'
    response = urllib.request.urlopen(url)
    data = response.read()
    character_data = json.loads(data)  
    
    return render_template("characters.html", characters=character_data['results'])

@app.route('/profile/<id>')
def get_profile(id):
    url = f'https://rickandmortyapi.com/api/character/{id}'  
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        profile_data = json.loads(data)
    except Exception as e:
        return f"Error fetching character profile: {e}"
    
    return render_template("profile.html", profile=profile_data)

@app.route('/lista')
def get_list_characters():
    url = 'https://rickandmortyapi.com/api/character'
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = json.loads(data) 
    
    characters_list = []
    
    for character in data_dict['results']:
        character_data = {
            'name': character['name'],
            'status': character['status'],
        }
        characters_list.append(character_data)
        
    return {'characters': characters_list}

@app.route('/locations')
def get_locations():
    url = 'https://rickandmortyapi.com/api/location'
    response = urllib.request.urlopen(url)
    data = response.read()
    locations_data = json.loads(data)    
    
    return render_template("locations.html", locations=locations_data['results'])

@app.route('/episodes')
def get_episodes():
    url = 'https://rickandmortyapi.com/api/episode'
    response = urllib.request.urlopen(url)
    data = response.read()
    episodes_data = json.loads(data)    
    
    return render_template("episodes.html", episodes=episodes_data['results'])

@app.route('/episode/<id>')
def get_episode(id):
    url = f'https://rickandmortyapi.com/api/episode/{id}'  
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        episode_data = json.loads(data)
        
        character_urls = episode_data.get('characters', [])
        characters = []

        for char_url in character_urls:
            try:
                char_response = urllib.request.urlopen(char_url)
                char_data = json.loads(char_response.read())
                characters.append(char_data)
            except Exception as e:
                print(f"Error fetching character: {e}")

    except Exception as e:
        return f"Error fetching episode: {e}"
    
    return render_template("episode.html", episode=episode_data, characters=characters)


@app.route('/location/<id>')
def get_location(id):
    url = f'https://rickandmortyapi.com/api/location/{id}'  
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        location_data = json.loads(data)
    except Exception as e:
        return f"Error fetching location: {e}"

    residents = []

    for resident_url in location_data.get('residents', []):
        try:
            resident_response = urllib.request.urlopen(resident_url)
            residents.append(json.loads(resident_response.read()))
        except Exception as err:
            return f"Error fetching resident: {err}"

    return render_template(
        "location.html",
        location=location_data,
        residents=residents
        )
