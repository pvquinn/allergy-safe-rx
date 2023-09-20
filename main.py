import requests
import json
def main():
    r = requests.get('https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=diphenhydramine')
    result = json.loads(r.text)
    print(result)
    new_pages = True
    while new_pages:
        if result['metadata']['next_page'] != 'null':
            result = json.loads(requests.get(result['metadata']['next_page_url']).text)
            for i in range(len(result['data'])):
                print(i.__str__() + '. ' + result['data'][i]['setid'] + ' --> ' + result['data'][i]['title'])
        else:
            new_pages = False

if __name__ == '__main__':
    main()
