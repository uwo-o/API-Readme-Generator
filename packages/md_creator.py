from email.policy import strict
from fileinput import filename
import json
import random
import string

def create_md(data):
    filename = ''
    for i in range(10):filename+=random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)

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
    with open('output/'+filename+'.md', 'w') as f:
        f.write('# ' + title + '\n')
        f.write('[![Version](https://img.shields.io/badge/version-' + version + '-brightgreen.svg)](' + url + ')')
        if license:
            f.write(' [![License](https://img.shields.io/badge/license-' + license + '-blue.svg)](' + license_url + ')')
        f.write('\n')
        f.write('\n')
        f.write(description + '\n')
        f.write('\n')
        if installation:
            f.write('* [Installation](#installation)\n')
        if usage:
            f.write('* [Usage](#usage)\n')
        if contributors:
            f.write('* [Contributing](#contributing)\n')
        if languages:
            f.write('* [Languages](#languages)\n')
        if technologies:
            f.write('* [Technologies](#technologies)\n')
        f.write('\n')
        if installation:
            f.write('## Installation\n')
            f.write('\n')
            for step in installation:
                f.write(step["step"] +'. '+ step["title"]+ '\n')
                f.write(step["description"] + '\n')
                if step["commands"]:
                    for command in step["commands"]:
                        f.write('\n')
                        f.write('``' + command + '``\n')

            f.write('\n')
        if(usage):
            f.write('## Usage\n')
            f.write('\n')
            for step in usage:
                f.write(step["step"] +'. '+ step["title"]+ '\n')
                f.write(step["description"] + '\n')
                if step["commands"]:
                    for command in step["commands"]:
                        f.write('\n')
                        f.write('``' + command + '``\n')
                if step["input"]:
                    for input in step["input"]:
                        f.write('\n')
                        f.write(input["description"]+'\n')
                        f.write('['+input["name"]+']('+input["url"]+')\n')
            f.write('\n')

        if(contributors):
            f.write('\n')
            f.write('## Contributing\n')
            f.write('\n')
            for contributor in contributors:
                f.write('* <img align="center" src="https://github.com/'+contributor["name"]+'.png" width="40px" style="border-radius:50%"></img> '+contributor["name"]+'\n')
                if contributor["social_media"]:
                    f.write('\n')
                    for social_media in contributor["social_media"]:
                        f.write('[!['+social_media["name"]+'](https://img.shields.io/badge/'+social_media["name"]+'-ffffff?style=for-the-badge&logo='+social_media["name"]+'&logoColor=black)]('+social_media["url"]+') ')
                f.write('\n')
            f.write('\n')
        if(languages):
            f.write('\n')
            f.write('## Languages\n')
            f.write('\n')
            f.write('* Languages used to create it: \n')
            f.write('\n')
            for language in languages:
                f.write('!['+language+'](https://img.shields.io/badge/'+language+'-ffffff?style=for-the-badge&logo='+language+'&logoColor=black) ')
            f.write('\n')
        if(technologies):
            f.write('\n')
            f.write('## Technologies\n')
            f.write('\n')
            f.write('* Technologies used to create it: \n')
            f.write('\n')
            for technology in technologies:
                f.write('!['+technology+'](https://img.shields.io/badge/'+technology+'-ffffff?style=for-the-badge&logo='+technology+'&logoColor=black) ')
            f.write('\n')
        if(keywords):
            f.write('\n')
            for keyword in keywords:
                f.write('!['+keyword+'](https://img.shields.io/badge/'+keyword+'-ffffff?style=for-the-badge&logo='+keyword+'&logoColor=black) ')
            f.write('\n')
        f.write('\n')
        f.write('---\n')
        f.write('Created by: ['+author+']('+author_url+')\n')

    # We return the message to the frontend.
    return filename