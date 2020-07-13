FROM mongo:3.2

#ADD ./initdb/seed.js /docker-entrypoint-initdb.d
COPY movieseed.json /scripts/seed.json
CMD  mongoimport --host mongodb --db movies --collection latestmovies --type json --file /scripts/seed.json --jsonArray --drop
