FROM python:3.9

# Workdir
WORKDIR /Exercise1

COPY src/ .

RUN pip install matplotlib plotly_express pandas numpy dash sklearn

# Runs when spinning up
CMD ["python", "src/ex1_0_setup.py" ]