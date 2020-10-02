#!/bin/sh
resourceGroupName=movieapp-rg
accountName=moviecosmos
dbName=movies
az group create --name $resourceGroupName --location UKSOUTH

az cosmosdb create \
    -n $accountName \
    -g $resourceGroupName \
    --default-consistency-level Session \
   
az cosmosdb database create --name $accountName --resource-group $resourceGroupName --db-name cloudwebapp
az cosmosdb mongodb database create --account-name $accountName \
                                    --name $dbName \
                                    --resource-group $resourceGroupName
                            