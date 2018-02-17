FROM python:3
RUN mkdir -p /opt/git_management_flask
WORKDIR /opt/git_management_flask
COPY ./requirements.txt /opt/git_management_flask
RUN pip install -r /opt/git_management_flask
COPY ./ /opt/git_management_flask
RUN cd /opt/git_management_flask && python setup.py install
