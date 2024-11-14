# Scheduler

## Preparation
To be able to push events to ur google calendar u need to specify `credentials.json` file.
In order to get a credentials file follow this steps:
1. Go to Google Cloud Console [[direct link](https://console.cloud.google.com/projectcreate)] and create new project
2. Select Navigation Menu <kbd>&#9776;</kbd> > Solutions > All Products > Google Auth Platform [[direct link](https://console.cloud.google.com/auth)]
3. Press <kbd>GET STARTED</kbd> and fill up information. In Audience section select External. (doesn't matter what you put in). Press <kbd>CREATE</kbd>
4. You should be redirected to Google Auth Platform page. From here select <kbd>Clients</kbd> > <kbd>CREATE CLIENT</kbd> [[direct link](https://console.cloud.google.com/auth/clients/create)]. In Application type select `Desktop app`. Name it whatever you want. Press <kbd>CREATE</kbd>
5. In `Actions` column press  <kbd>Download OAuth client</kbd> > <kbd>DOWNLOAD JSON</kbd>. Save it as `credentials.json` at `.creds/`. Full path should be `Scheduler/creds/credentials.json`
6. Select Audience > <kbd>ADD USERS</kbd> > Type your email > <kbd>SAVE</kbd>
7. Done

## Run
* Create virtual environment if needed `python -m venv venv`
* Install requirements  `pip install requirements.txt -r`
* Run app `python main.py`
