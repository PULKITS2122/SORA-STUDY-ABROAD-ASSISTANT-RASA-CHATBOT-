# International Office Assistant(Rasa ChatBot)

_Members:_

| Name (First and Last Name) | Matriculation  |
| -------------------------- | -------------- |
| Aryan Jain                 | 22107593       |
| Pulkit Sharma              | ---------------|

**Project Title: International study abroad chatbot"**

GIT LINK: 

WIKI LINK: 

# Project Description
A useful chatbot developed with Python and Rasa, designed to assist new incoming students by addressing their admission queries and providing accurate information and guidance.

# Prerequisites
To run this project on your computer, you will need the following software and libraries:
1. Python [3.8]
2. Rasa [3.1]

# Installation
## Setup and Usage
In order to use this chatbot offline on your personal system, follow the steps below:
- Download or clone this repository using the following command:

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
Aryan Jain:
1. Developed the domain, NLU, and story components.
2. Crafted dialogues and structured them into a coherent flow.
3. Implemented classes in actions to ensure the chatbot responds appropriately.
4. Designed 2 user personas.
5. Contributed to the development and testing of stories.

Pulkit Sharma:
1. Developed the domain, NLU, and stories.
2. Crafted dialogues and organized them into a logical flow.
3. Developed and documented critical use cases.
4. Established rules for the chatbot.
5. Implemented action classes to ensure appropriate chatbot responses.
6. Created one system persona and one user persona.

