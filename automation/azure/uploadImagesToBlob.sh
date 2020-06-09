#!/bin/sh
STORAGEACCOUNT=moviestoragerom
if [[ $(az storage account check-name --name $STORAGEACCOUNT --query 'nameAvailable') != 'true' ]]
then  
    echo "Storage account $STORAGEACCOUNT already exists";    
else
    echo "About to create $STORAGEACCOUNT"
    az storage account create -n $STORAGEACCOUNT -g movieapp-rg -l westus --sku Standard_LRS
fi
