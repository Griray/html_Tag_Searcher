import yaml
from urllib.parse import urlparse, urlunparse

with open('aliases.yaml', encoding='utf-8') as file:
    dns_aliases = yaml.load(file, Loader=yaml.FullLoader)


def resolve_aliases(url: str) -> str:
    parsed_url = urlparse(url)
    if parsed_url.netloc not in dns_aliases:
        return url
    parsed_url = parsed_url._replace(netloc=dns_aliases[parsed_url.netloc])
    return urlunparse(parsed_url)
