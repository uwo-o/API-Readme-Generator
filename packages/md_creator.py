def create_md(data):

    # We get the parameters from the JSON file.
    title = data["title"]
    description = data["description"]
    url = data["url"]
    license = data["license"]
    license_url = data["license_url"]
    version = data["version"]
    author = data["author"]
    author_url = data["author_url"]
    contributors = data["contributors"]
    repository = data["repository"]
    repository_url = data["repository_url"]
    keywords = data["keywords"]
    languages = data["languages"]
    technologies = data["technologies"]
    installation = data["installation"]
    usage = data["usage"]

    # We create the MD file.
    with open('output/README.md', 'w') as f:
        f.write('# ' + title + '\n')
        f.write('[![Version](https://img.shields.io/badge/version-' + version + '-brightgreen.svg)](' + url + ')')
        if(license):
            f.write(' [![License](https://img.shields.io/badge/license-' + license + '-blue.svg)](' + license_url + ')')
        f.write('\n')
        f.write('\n')
        f.write(description + '\n')
        f.write('\n')
        f.write('## Table of Contents\n')
        f.write('\n')
        f.write('* [Installation](#installation)\n')
        f.write('* [Usage](#usage)\n')
        f.write('* [Contributing](#contributing)\n')
        f.write('\n')
        f.write('## Installation\n')
        f.write('\n')
        for step in 
        f.write('## Usage\n')
        f.write('\n')
        f.write('## Contributing\n')
        f.write('\n')
        f.write('---\n')
        f.write('Created by: ['+author+']('+author_url+')\n')

    # We print the message to the console.
    print('README.md file created.')

    # We return the message to the frontend.
    return 'README.md file created.'