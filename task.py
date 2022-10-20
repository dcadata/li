import json


def main():
    links = json.load(open('config/links.json'))
    template = open('config/template.html').read()
    for link in links:
        with open(f'{link["filename"]}.html', 'w') as f:
            f.write(template.format(**link))


if __name__ == '__main__':
    main()
