FROM golang:1.16

WORKDIR /usr/src/app

COPY ./example-backend .

RUN go mod download && go mod verify


RUN go build

RUN chmod +x ./server

CMD ["./server"]
