import requests
import json

def convert_to_shorte(URL):
    response = requests.put("https://api.shorte.st/v1/data/url",
                            {"urlToShorten": URL}, headers={"public-api-token": "YOUR API TOKEN"})
    decoded_response = json.loads(response.content)
    ReturnVal = (decoded_response['shortenedUrl'])
    return ReturnVal

def main():
    print (convert_to_shorte("www.google.com"))

if __name__ == '__main__':
    main()
