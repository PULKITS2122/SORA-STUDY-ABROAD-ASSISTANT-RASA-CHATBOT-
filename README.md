# NOA STUDY ABROAD ASSISTANT (RASA CHATBOT)

_Members:_

| Name (First and Last Name)| Matriculation |
| ------ | ------ |
| Pulkit Sharma | 22201100 |
| Aryan Jain | 22107593 |

**Project Title: International study abroad chatbot - "Noa"**

GIT LINK : https://mygit.th-deg.de/db30158/project-noa.git

WIKI LINK : https://mygit.th-deg.de/db30158/project-noa/-/wikis/home

# Project Description
A helpful chatbot which is build using Python and Rasa. The aim of this chatbot is to help all the new incoming students with their admission queries and to provide them with proper answers and guidance.

# Prerequisites
To run this project on your computer, you will need the following software and libraries:
1. Python [3.8]
2. Rasa [3.1]

# Installation
## Setup and Usage
In order to use this chatbot offline on your personal system, follow the below steps:
- Download or clone this repository using following command:
```
git clone https://mygit.th-deg.de/db30158/project-noa.git
```
- Go to the cloned directory and install virtualenv package (if you don't have it already)
```
cd project_noa 
pip install virtualenv
```
- Create a new virtual environment in current directory with specified version of Python and activate it
```
python -m venv env

.\env\Scripts\activate.bat (on windows)
source env/bin/activate (on mac/linux)
```
`Note: Python3.8 is the recommanded Python version for this project. Install and add it to PATH incase there are any errors.`
- Next step is to install Rasa and train the model
```
pip install Rasa
rasa train
```
- To connect port, open another terminal, activate virtual environment and run following command
```
rasa run actions
```
- Open previous terminal and enter following command to start interacting with chatbot
```
rasa shell
```

## Contributions
Don Binoy:
1. Worked on domain, nlu and stories.
2. Created dialogs and converted it into a flow
3. Created critical use case and documented it.
4. Implemented classes in actions for chatbot to reply accordingly.
5. Created a system and 2 user personas.

Avanish Kumar Singh:
1. Worked on domain, nlu and stories.
2. Created dialogs and converted it into a flow.
3. Created rules for chatbot.
4. Implemented classes in actions for chatbot to reply accordingly.
5. Created 1 user personas.
6. Worked on test stories.
