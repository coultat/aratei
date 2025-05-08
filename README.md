ARATEI


Aratei means sunday in the Guarani language. A language spoken in Paraguay, South of Brazil and a part from Argentina.


This project is intended to integrate different music apis (as an integration exercise), having all of it tested,
with interfaces, dockers and more tools. The project was created in my free time beginning on a random sunday at home
when my kids were sleeping (that's why the name arateĩ).

What does the project do?
The app is in charge of:
- Exposes a REST API using FastAPI.
- Asynchronously fetches data from different music APIs (Spotify, Deezer, etc.)
- Mapps the data using pydantic models.
- Stores the data in a PostgresSQL database.
- Executed in Docker containers.
- Tested with pytest


<h2>How to use it?</h2>
1 Clone the repository
```bash
git clone https://github.com/tu-usuario/aratei.git
cd aratei
```

2 Install the requierements
```bash
python -m venv .env
source .env/bin/activate
pip install requirements.txt-
```

3 Run Docker
```bash
docker-compose up --build
```


Known issues and missing parts:
- [] Implement SQLAlchemy<br>
- [] Implement Dockers<br>
- [] Extend the use for Playlists, Songs and more<br>
- [] Implement Celery Tasks<br>
