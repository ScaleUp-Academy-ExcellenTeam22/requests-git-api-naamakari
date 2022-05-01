import requests
import sys
from typing import Tuple


def get_username_and_token() -> Tuple:
    """
    The function receives nothing and returns input from the command line that contains the username and token.
    :return: Tuple of the username and the token.
    """
    return sys.argv[1], sys.argv[2]


def prints_nicely_to_the_screen(repository: Tuple, programming_language: str) -> None:
    """
    The function receives a repository and prints it nicely, according to the received language.
    :param repository: The received repository.
    :param programming_language: The language in which the repository is written.
    """
    print(f"{repository[0]} is a {programming_language} repo with {repository[1]} stars.")


def top_repositories_from_github(programming_language: str, number: int, input_function, output_function) -> None:
    """
    The function receives a language and a number, and brings from the GitHub the number of repositories according
    to the number and language received, arranged according to the number of stars in descending order.
    :param programming_language: The language in which you want the repositories.
    :param number: The language in which you want the repositories.
    :param input_function: The function from which the current function receives input.
    :param output_function: The function to which the current function sends the output.
    """
    headers = {"Accept": "application/vnd.github.v3+json"}
    username, token = input_function()
    response = requests.get("https://api.github.com/search/repositories?q=language:" + programming_language +
                            "&sort=stars&order=desc", headers=headers, auth=(username, token))
    repositories = response.json()['items']
    repositories = [(item['name'], item['stargazers_count']) for i, item in enumerate(repositories) if i < number]
    for repository in repositories:
        output_function(repository, programming_language)


if __name__ == '__main__':
    top_repositories_from_github('Python', 20, get_username_and_token, prints_nicely_to_the_screen)
