# Syntactic Sugar

Project for Goldman Sachs Warsaw Hackathon 2022.

### Problem Definition:

### Our Solution:

### Impact:


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