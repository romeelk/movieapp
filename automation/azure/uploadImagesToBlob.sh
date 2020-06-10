#!/bin/sh
STORAGEACCOUNT=moviestoragerom
if [[ $(az storage account check-name --name $STORAGEACCOUNT --query 'nameAvailable') != 'true' ]]
then  
    echo "Storage account $STORAGEACCOUNT already exists";    
else
    echo "About to create $STORAGEACCOUNT"
    az storage account create -n $STORAGEACCOUNT -g movieapp-rg -l westus --sku Standard_LRS
fi
az storage container create -account-name $STORAGEACCOUNT -name movieimages
ACCOUNTKEY=$(az storage account keys list --account-name moviestoragerom --query [0].value)
az storage blob upload-batch -d movieimages -s ../../src/web/movieapp/static/images/ --account-key $ACCOUNTKEY --account-name $STORAGEACCOUNT
