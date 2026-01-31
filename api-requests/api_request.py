import requests

# Keep the key here
API_KEY = ""
BASE_URL = "http://api.weatherstack.com/current"

def fetch_data(city):
    """
    Fetches data for a SPECIFIC city passed as an argument.
    """
    # Construct the URL dynamically for the specific city
    params = {
        'access_key': API_KEY,
        'query': city
    }

    try: 
        # Pass params correctly to requests
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if the API sent a logic error (like 429 Rate Limit inside JSON)
        if 'error' in data:
            print(f"API Error for {city}: {data['error']['info']}")
            return None

        print(f'Successfully fetched data for {city}')
        return data

    except requests.exceptions.RequestException as e:
        print(f'Error Fetching Data: {e}')
        return None

def fetch_mock_data():
    # (Keep your existing mock data function here if you want)
    pass