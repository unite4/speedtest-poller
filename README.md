# Speedlog Poller
A Python application that runs a Speedtest and saves results in the Firebase Realtime Database.

# Running a Docker
Docker instance runs application every 15 minutes by default.

```bash
$ ./run-docker.sh
```

It is also possible to define own time interval, for instance:

```bash
$ ./run-docker.sh 1h
```

# Running a single test

## Configure Firebase

### Certificate

Generate the Firebase private key:

1. Login to the [Firebase console](https://console.firebase.google.com/)
2. Choose existing or create a new project
3. Go to project settings
4. Go to "Service accounts" tab
5. Click on the "Generate new private key" button

Put newly generated file in `firebase/certificate.json`.

### Config

Create a configuration file in `firebase/config.json` with JSON:

```json
{
  "databaseURL": "https://your-firebase-project.firebaseio.com/"
}
```

More available parameters: https://firebase.google.com/docs/reference/admin/python/firebase_admin#initialize_app.

## Setup environment

```bash
$ virtualenv .environment
```

```bash
$ source .environment/bin/activate
```

```bash
$ export FIREBASE_CERTIFICATE=firebase/certificate.json
```

```bash
$ export FIREBASE_CONFIG=firebase/config.json
```

## Install dependencies

```bash
$ pip install -r requirements.txt
```

## Run application

```bash
$ python run-poller.py
```
