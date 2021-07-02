![Python package](https://github.com/romeelk/movieapp/workflows/Python%20package/badge.svg)

# Movie App - Python Flask

## Sample container app

A Sample container app to guide myself through the best practises for k8s on Azure (AKS)

The app is a fictional movie catalog app that provides a catalog of latest movies with their associated 
reviews.

The stack being used is:
* Frontend - Apache Flask
* Backend  - A couple of REST APIs
* Mongodb/cosmosdb

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
* Keep secrets out of configuration (API Keys, connection strings)

## Pre-requisites

* An AWS account. I use s3 bucket to store the landing page images
* Azure account for Cosmosdb
* Azure and AWS clis 
* Hahsicorp Vault locally

## Running the app locally using docker compose

To build the app using docker compose run the following command:

```
docker-compose build --no-cache 
```

To bring up the container use:

```
docker-compose -f docker-compose.yml -f docker-compose-ci.yml up
```

## Running the app using K8s locally

You can enable Kubernetes locally on Docker desktop. Once you have done that
make sure you switch context to the docker-desktop cluster. Easy way to do this is to install
the VS code K8s extension. Go to the extension. In the clusters list select docker-desktop and
set as current cluster.

There are two steps to deploying. First add helm  mongodb repo locally using the bitnami helm chart:

Generate a password for Mongodb:

## Secrets management 

For this example I am using Hahicorp vault. Please follow to install it:
https://www.google.com/search?q=install+vault&oq=install+vault&aqs=chrome..69i57j69i60.1967j0j7&sourceid=chrome&ie=UTF-8

Start the vault in dev mode
``` 
vault server -dev
```

In another terminal start the client

```
export VAULT_ADDR='http://127.0.0.1:8200'
```

first create a secrets for the movieapp:

Generate password for mongodb pod

```
password=$(curl --silent https://www.passwordrandom.com/query?command=password)
```
Set the secret in vault:

```
vault secrets enable -path=movieapp kv
vault kv put secret/movieapp MONGO_PASSWORD=$password
```

Verify secret:
```
password=$(vault kv get -field MONGO_PASSWORD secret/movieapp)
```


## Installing mongodb via Helm

```
helm repo add bitnami https://charts.bitnami.com/bitnami

helm install moviedb bitnami/mongodb --set auth.username=movieapp,auth.password=$password,auth.database=movies
```
The following output is printed below (password export statements omitted):

```

NAME: moviedb
LAST DEPLOYED: Sun Oct 25 22:26:33 2020
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

MongoDB can be accessed via port 27017 on the following DNS name(s) from within your cluster:

    moviedb-mongodb.default.svc.cluster.local

To get the root password run:

    export MONGODB_ROOT_PASSWORD=$(kubectl get secret --namespace default moviedb-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 --decode)

To connect to your database, create a MongoDB client container:

    kubectl run --namespace default moviedb-mongodb-client --rm --tty -i --restart='Never' --image docker.io/bitnami/mongodb:4.4.1-debian-10-r39 --command -- bash

Then, run the following command:
    mongo admin --host "moviedb-mongodb" --authenticationDatabase admin -u root -p $MONGODB_ROOT_PASSWORD

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/moviedb-mongodb 27017:27017 &
    mongo --host 127.0.0.1 --authenticationDatabase admin -p $MONGODB_ROOT_PASSWORD
```

Create the secret for the mongodb db
```
kubectl create secret generic movieappsecret --from-literal=mongodburi=mongodb://root:$MONGODB_ROOT_PASSWORD@moviedb-mongodb.default.svc.cluster.local
```

Reference the secret in the deployment manifest for the movieapi pod as follows:

```
env:
    - name: MONGO_DBNAME
        value: movies
    - name: MONGO_URI
        valueFrom:
            secretKeyRef:
            name: movieappsecret
            key: mongodburi
```

Once this is done deploy:

```
kubectl apply -f deployment-local.yaml 
```

# Github lint

The project uses https://github.com/marketplace/actions/lint-action

to lint the python files.