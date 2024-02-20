import requests
def keyword_finder(text,lang): #en or fa
    url = "https://api.edenai.run/v2/text/keyword_extraction"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "providers": "ibm",
        "language": str(lang), #en or #fa
        "text": str(text)
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjhlOTMxYmYtMzgxYS00NWUxLWExNWEtYWJmNWEzZDE2YTcwIiwidHlwZSI6ImFwaV90b2tlbiJ9.GedqQ1ClFdRA7LpTgTYNXnMsfud891IECYAvUhyOzYg"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text

def text_summarizer(text):
    url = "https://api.edenai.run/v2/text/summarize"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "output_sentences": 1,
        "providers": "alephalpha",
        "text": str(text),
        "language": "en"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjhlOTMxYmYtMzgxYS00NWUxLWExNWEtYWJmNWEzZDE2YTcwIiwidHlwZSI6ImFwaV90b2tlbiJ9.GedqQ1ClFdRA7LpTgTYNXnMsfud891IECYAvUhyOzYg"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text


print(text_summarizer("In the heart of a bustling city, amidst towering skyscrapers and bustling streets, lies a hidden oasis of tranquility. Here, time slows down, and the gentle rustling of leaves in the breeze replaces the constant hum of traffic. A quaint little café nestled in a quiet corner serves aromatic coffee and freshly baked pastries, where locals and tourists alike gather to savor moments of respite from the chaos outside"))