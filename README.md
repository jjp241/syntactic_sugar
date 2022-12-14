# Syntactic Sugar

Project for Goldman Sachs Warsaw Hackathon 2022.

### Link to our 5 minute video presentation:
https://drive.google.com/file/d/13Nu_U5iX_ofohM_L8YMUj3I8uHPRfpcq/view?usp=share_link

### Problem Definition:
 - People in IT don’t know what Goldman Sachs does, and what they can do here.
 - The Goldman Sachs booth is not interesting and people are not keen on completing forms, which would enable Goldman Sachs to collect data about potential candidates.
 - Even when people interact at the booth, they don’t stay in the loop and stay interested in Goldman Sachs - bad retention
 - The recruitment process is lengthy, thus offsetting

### Our Solution:
Our idea is to create a platform where people can learn more about teams in Goldman Sachs, and occasionally win prizes. We collect data about what they click on, on our platform, so we don’t need to ask them to fill job interests form. 

We want to make them feel part of the community and keep them in the loop, by giving them a unique hardware gadget, that attracts them to platform and reminds them of it after conference - GoldToken

### Impact:
 - People at the event are more interested in the booth and completing forms and leaving their data
  - IT Specialists are interested in Goldman Sachs actions and teams, they understand what Goldman Sachs does, and they see Goldman Sachs as a potential workplace
  - Our information gathering process is simplified, less mundane for candidate, and seamless for HR department (50% faster) (thing such as the candidates interests are collected, when the candidate uses our platform)

## :hammer_and_wrench: Running Locally :hammer_and_wrench:

#### 1. Clone Repo

#### 2. Instal requirements for flask app:

`pip install -r requirements.txt` 

#### 3. Install `npm` and `yarn` and dependencies for stockmarket simulation:

```
sudo apt install npm
sudo npm install --global yarn
cd stockmarket-simulation
yarn install
cd ..
```

#### 4. Run script that runs everything for you!

```
chmod a+x run.sh
./run.sh
```

Now you can see our app on `localhost:5000` :heart:

#### 5. To kill the server, just run another script:

```
chmod a+x stop.sh
./stop.sh
```

## Implemented Solution
### Platform
We implemented a version of our platform with one flow - from logging into our system and activating the token id, through choosing a team, to
seeing the challenges, games and quizzes related to that team. However this is easily scalable as the logic for each flow is the same as the one we implemented (the only differences are the challenges/games/quizzes for each team).

When choosing the team we show a short teams description, in order for the user to get a high level overview of what the team does and if they are interested in doing the challenges/games/quizzes associated with tat team.

During completing the challenges/games/quizzes the user collects point, which encourages them to keep playing and completing more courses.

Each move (click) of where the user goes is collected to our database.

### GoldToken
We implemented a prototype working version of our GoldToken. We can show how it works on our devices. We also enable entering the token id, by hand in case if the user was to for example get the token id by mail.

3D model was done in Autodesk Fusion360.

Gold Token is implemented by regular pendrive, with `user-token.json` where the unique ID is saved. After plugging to device and clicking `Proceed` our backend scans for this file in USB devices.

Then loads this ID from token, and proceeds further in app.

### Database
We mocked a database to collect the user data, and user analytics data (our 
mocked database is in the form of a json file which collects all of this information, 
with parts of it hardcoded - such as the analytics since we only implemented the flow for the quant team).

This is a model, in the form of a json, of how and what data we keep:
```
{
    "user_data": [
        {
            "token-id": "test1token",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "email@email.com",
            "uni_name": "University of Warsaw",
            "major": "Computer Science",
            "sex": "Female"
        },
    ],
    "user_analytics_data": [
        {
            "token-id": "test1token",
            "team": "quant"
        }
    ]
}
```

### Admin Panel
We also implemented a mock of the admin panel, through which HR can filter candidates
by the event they attended, their token id etc. 

They can access data to all of the users data as well as the collected users analytics data. 
This makes it easier to reach out to potential candidates, which will make the recruitment process faster and smoother.

### Stockmarket simulation 
We've used an open source solution, which we tinkered with to make it work for our use case. Actually, on a branch 'news' we imroved the news feed feature that was in developement on a official release of package. 


