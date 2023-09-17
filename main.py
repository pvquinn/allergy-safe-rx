import requests
def main():
    r = requests.get('https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=diphenhydramine')
    print(r.text)


if __name__ == '__main__':
    main()
