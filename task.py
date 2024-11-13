import json
import os

_BASE_URL = 'https://ankar.io/li/'


def main() -> None:
    links = json.load(open('config/links.json'))
    template = open('config/template.html').read()

    readme_sections = ['# Links\n', '|Title|Filename|From|To|', '|-|-|-|-|']
    for link in links:
        with open('{filename}.html'.format(**link), 'w') as f:
            f.write(template.format(**link))
        readme_sections.append('|{title}|`{filename}`|{base_url}{filename}|{url}|'.format(**link, base_url=_BASE_URL))

    with open('README.md', 'w') as f:
        f.write('\n'.join(readme_sections))

    unused_filenames = {fn.split('.html')[0] for fn in os.listdir('.') if fn.endswith('.html')} - {
        link['filename'] for link in links}
    for unused_fn in unused_filenames:
        os.remove(f'{unused_fn}.html')

    return


if __name__ == '__main__':
    main()
