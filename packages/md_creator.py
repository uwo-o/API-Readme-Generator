def create_md(data):

    # We get the parameters from the JSON file.
    title = data['title']
    description = data['description']
    url = data['url']
    license = data['license']
    license_url = data['license_url']
    version = data['version']
    author = data['author']
    author_url = data['author_url']
    repository = data['repository']
    repository_url = data['repository_url']
    keywords = data['keywords']

    # We create the MD file.
    with open('output/README.md', 'w') as f:
        f.write('# ' + title + '\n')
        f.write('\n')
        f.write(description + '\n')
        f.write('\n')
        f.write('[![License: ' + license + '](https://img.shields.io/badge/License-' + license + '-blue.svg)](' + license_url + ')\n')
        f.write('\n')
        f.write('[![Version](https://img.shields.io/badge/version-' + version + '-brightgreen.svg)](' + url + ')\n')
        f.write('\n')
        f.write('[![Github](https://img.shields.io/badge/Github-[![Github](https://www.github.com/uwo-o' + repository + ')]-brightgreen.svg)](' + repository_url + ')\n')
        f.write('\n')
        f.write('[![Author](https://img.shields.io/badge/Author-' + author + '-brightgreen.svg)](' + author_url + ')\n')
        f.write('\n')
        f.write('[![Keywords](https://img.shields.io/badge/Keywords-' + keywords + '-brightgreen.svg)](' + url + ')\n')
        f.write('\n')
        f.write('\n')
        f.write('## Table of Contents\n')
        f.write('\n')
        f.write('* [Installation](#installation)\n')
        f.write('* [Usage](#usage)\n')
        f.write('* [License](#license)\n')
        f.write('* [Contributing](#contributing)\n')
        f.write('* [Tests](#tests)\n')
        f.write('* [Questions](#questions)\n')
        f.write('\n')
        f.write('## Installation\n')
        f.write('\n')
        f.write('\n')
        f.write('## Usage\n')
        f.write('\n')
        f.write('\n')
        f.write('## License\n')
        f.write('\n')
        f.write('\n')
        f.write('## Contributing\n')
        f.write('\n')
        f.write('\n')
        f.write('## Tests\n')
        f.write('\n')
        f.write('\n')
        f.write('## Questions\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')

    # We print the message to the console.
    print('README.md file created.')

    # We return the message to the frontend.
    return 'README.md file created.'