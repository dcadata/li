import json


def main():
    links = json.load(open('config/links.json'))
    template = open('config/template.html').read()
    readme_sections = ['# Links']

    for link in links:
        with open(f'{link["filename"]}.html', 'w') as f:
            f.write(template.format(**link))
        readme_sections.append('* [{title}]({url}) `{filename}`'.format(**link))

    readme = '\n\n'.join(readme_sections)
    with open('README.md', 'w') as f:
        f.write(readme)


if __name__ == '__main__':
    main()
