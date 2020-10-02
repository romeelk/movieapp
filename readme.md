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
* Keep secrets out of configuration (API Keys)

## Running the app using docker compose

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
the vs code K8s extension. Go to the extension. In the clusters list select docker-desktop and
set as current cluster.

There are two steps to deploying. First deploy a mongodb locally using the bitnami helm chart:

helm repo add bitnami https://charts.bitnami.com/bitnami

password = $(curl --silent https://www.passwordrandom.com/query?command=password)

## Secrets management 

For this example I am using Hahicorp vault. Please follow to install it:
https://www.google.com/search?q=install+vault&oq=install+vault&aqs=chrome..69i57j69i60.1967j0j7&sourceid=chrome&ie=UTF-8

first create a secrets engine for the movieapp:

```
vault secrets enable -path=movieapp kv
```

Get the secret as follows

```
password=$(vault kv get -field MONGO_PASSWORD movieapp/config)
```
## Installing mongodb via Helm

```
helm install ratings bitnami/mongodb \ 
    --set auth.username=movieapp,auth.password=$password,auth.database=movies
```
The following output is printed below (password export statements omitted):

```
MongoDB can be accessed via port 27017 on the following DNS name from within your cluster:
    mongodb-1592347563.default.svc.cluster.local
```

Record the name of the mongodb fqdn within the cluster e.g  mongodb-1592347563.default.svc.cluster.local
Record the root password env var $MONGODB_ROOT_PASSWORD to be used in a connection string: 

```
kubectl port-forward --namespace default svc/mongodb-1592347563 27017:27017 &
mongo --host 127.0.0.1 --authenticationDatabase admin -p $MONGODB_ROOT_PASSWORD
```



```
kubectl create secret generic movieappsecret --from-literal=mongodburi=mongodb://root:$MONGODB_ROOT_PASSWORD@mongodb-1592347563.default.svc.cluster.local:27017/
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

