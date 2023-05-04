# Running (local)

## First time setup
1. Install Python;
2. Create a virtual environment: `python -m venv .venv`;
3. Activate the environment: `. .venv/bin/activate`;

## Usage
1. Activate the environment: `. .venv/bin/activate`;
2. Install/update the packages inside environment: `pip install -r requirements.txt`;
3. Create migrations: `python manage.py makemigrations`;
4. Run migrations: `python manage.py migrate`;
5. Start the server: `python manage.py runserver`.

## Using
- Survey page at http://localhost:8000/;
- Thank you page at http://localhost:8000/thank_you;
- Results page at http://localhost:8000/results.


