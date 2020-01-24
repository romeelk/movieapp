# K8S Labs

## Sample container app

A Sample container app to guide myself through the best practises for k8s on Azure (AKS)

The app is a fictional movie catalog app that provides a catalog of latest movies with their associated 
reviews.

The stack being used is:
* Frontend - Apache Flask
* Backend  - A couple of REST APIs
* Redis - have not decided yet!!

The aim is to use this reference app to place the front end and backend into containers. Push it to
a secure container registry (ACR). Then make it ready for AKS. Optionally deploy it to Web App for containers
as well using a docker-compose file.

## Things to think about

This is not a production ready application. Please note Flask applications should be wrapped behind a reverse
proxy such as nginx. However, my aim is to demonstrate modern Cloud based application using the principles discussed
in the 12 factor app:

Here are a few:
* Backing services (Azure or AWS - blob storage, cosmos db)
* Externalised config from application code through environment variables
* Keep secrets out of configuration (API Keys)

