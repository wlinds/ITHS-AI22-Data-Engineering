FROM python:3.11

# Host container
ADD main.py .

RUN pip install plotly_express dash

# Runs when spinning up
CMD ["python", "./main.py" ]