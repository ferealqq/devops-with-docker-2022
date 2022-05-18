FROM golang:1.16-alpine as build

WORKDIR /usr/src/app

COPY ./example-backend .

RUN CGO_ENABLED=0 go build -ldflags "-s -w" -o server

FROM scratch as runner
COPY --from=build /usr/src/app/server /opt/app/
CMD ["/opt/app/server"]