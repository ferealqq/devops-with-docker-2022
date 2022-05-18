FROM node:16-alpine as build-stage

WORKDIR /app

COPY ./example-frontend .


RUN npm i --silent --production && npm run build && \
    find /app -mindepth 1 -not -regex '^/app/build.*' -delete
    
# CMD ["serve", "-s", "-l", "5000", "build"]

FROM nginx:1.19-alpine

EXPOSE 80

ENV REACT_APP_BACKEND_URL="http://127.0.0.1/api"
COPY --from=build-stage /app/build/ /usr/share/nginx/html