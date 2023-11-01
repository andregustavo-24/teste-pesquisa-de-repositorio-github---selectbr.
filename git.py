import requests

def search_github_reositories(query):
    base_url = "https://api.github.com/search/repositories"
    params = {
        "q": query
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        for repo in data['items']:
            print(f"nome: {repo['name']}")
            print(f"descrição: {repo['description']}")
            print(f"URL: {repo['html_url']}")
            print("----")
    else:
        print(f"falha na solicitação. codigo de status: {response.status_code}")

"if_name_"=="_main_"
query = input("digite sua consulta  de repositorio github:")
search_github_reositories(query)