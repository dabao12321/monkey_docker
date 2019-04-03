FROM python:3
WORKDIR /testing
COPY . /testing
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python"]
