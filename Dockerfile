FROM python:3.7-slim


WORKDIR /usr/src
#RUN apk --update add python-dev
# Ensure that directories and files for mounted volumes are created.
# Copy source code
RUN apt update && apt install -y python3-dev build-essential ca-certificates
COPY . .
RUN pip install shiv
RUN python setup.py bdist_wheel
#ENV SHIV_INTERPRETER /usr/local/bin/python
RUN shiv -c trlarry -o dist/larry_server dist/trlarry-0.0.1-py3-none-any.whl


FROM python:3.7-slim
WORKDIR /usr/bin
COPY --from=0 /usr/src/dist/larry_server .
RUN mkdir .shiv
RUN chmod +x larry_server
ENV SHIV_ROOT /usr/bin/.shiv
EXPOSE 50051
CMD ["./larry_server"]

