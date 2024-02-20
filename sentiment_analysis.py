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


print(text_summarizer("To display the histogram of keyword importance below the insert text box, you can modify the HTML page to include a new div element where the histogram will be displayed. You can use JavaScript to parse the JSON data returned by the Flask function and create the histogram dynamically. Here's the modified HTML code:"))