# Interview: Star Wars
This simple project was made as a task for one of my interview processes which I had.
Task description is present in PDF document in `docs` directory.

# Pre-requirements
```bash
ngrok  # or working SWAPI
npm
yarn
node
Python3
```

## Prepare .env file
Create your `.env` file using below command:

```bash
echo "SWAPI_URL=http://<YOUR_UNIQUE_INSTANCE_ID>.ngrok.io/api/" > .env
```
SWAPI instance can be hosted from your local machine. Please use this project from GitHub: https://github.com/lahim/interview-swapi
and follow by instructions.
SWAPI should be covered by the Ngrok (https://ngrok.com/docs) using below command:
```bash
ngrok http 5000
```

# How to run it?
You can run in using Docker or your command line.

## Run with Docker
```bash
docker-compose up --build
```

Backend will be available under below url:
```bash
http://localhost:8000/
```

Frontend will be available under below url:
```bash
http://localhost:8080/
```

## Run with command line
Backend can be run using below commands:
```bash
export $(cat .env)
cd backend
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt
./manage.py migrate
./manage.py collectstatic
./manage.py runserver
```

Frontend can be run using below commands:
```bash
cd frontend
yarn
yarn build
yarn serve
```
