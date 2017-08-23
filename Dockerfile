FROM swernst/cauldron:latest-miniconda

RUN pip install plotly && \
    mkdir /output

COPY workshop-example /project/workshop-example
COPY run.py /project/run.py

ENTRYPOINT ["python", "/project/run.py"]
