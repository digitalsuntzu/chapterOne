import requests

def fetch_data(url):
    """ Fetches data from a given URL. """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    
if __name__=="__main__":
    api_url = "https://www.google.com"
    data = fetch_data(api_url)
    print(data)
