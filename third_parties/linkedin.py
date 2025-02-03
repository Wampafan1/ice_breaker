import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkindin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from a linkedin profiles, 
    Manually scrape the information from a linkedin profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Wampafan1/2d4395bcda4ff7594d9ad6545e64ab6b/raw/98768381519506bb2e5eb51a2f142e705fdff278/joe-delghingaro-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.getenv("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["certifications", "languages"]
    }

    return data

if __name__ == "__main__":
    print(
        scrape_linkindin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/the-real-joe/", mock=True
        )
    )