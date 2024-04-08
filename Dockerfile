FROM python:3.9-buster


RUN apt-get clean && apt-get update
RUN python -m pip install --upgrade pip

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

ENTRYPOINT ["python", "main.py"]