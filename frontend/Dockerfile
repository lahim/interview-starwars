FROM node:12.16.2-slim

RUN mkdir -p /app/frontend/

WORKDIR /app/frontend/

COPY . .

RUN npm rebuild node-sass && \
    yarn && \
    yarn build

EXPOSE 8080

CMD ['bash', 'run.sh']
