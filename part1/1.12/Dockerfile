FROM node:16


COPY ./example-frontend .

EXPOSE 5000

RUN npm i && npm run build && npm i -g serve

CMD ["serve", "-s", "-l", "5000", "build"]
