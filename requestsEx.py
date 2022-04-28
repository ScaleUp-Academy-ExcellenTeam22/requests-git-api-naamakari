import requests
import sys


def top_repository_from_github(programming_language: str, number: int):
    """
     The function receives a language and a number, and brings from the GitHub the number of repositories according
     to the number and language received, arranged according to the number of stars in descending order.
    :param programming_language: The language in which you want the repositories.
    :param number: The number of repositories we want.
    """
    headers = {'Accept': 'application/vnd.github.v3+json'}
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get('https://api.github.com/search/repositories?q=language:' + programming_language +
                            '&sort=stars&order=desc', headers=headers, auth=(username, token))
    repositories = response.json()['items']
    repositories = [(item['name'], item['stargazers_count']) for i, item in enumerate(repositories)
                    if i < number]
    list(map(lambda value: print(f"{value[0]} is a {programming_language} repo with {value[1]} stars."), repositories))


if __name__ == '__main__':
    top_repository_from_github('Python', 20)
