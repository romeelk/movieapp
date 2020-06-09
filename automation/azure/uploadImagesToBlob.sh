#!/bin/sh
STORAGEACCOUNT=moviestorage$RANDOMaccount
if [[ $(az storage account check-name --name $STORAGEACCOUNT --query 'nameAvailable') = 'true' ]]
then  
    echo "Storage account $STORAGEACCOUNT already exists"; 
else
   echo "About to create $STORAGEACCOUNT"
#    aws s3api create-bucket --bucket $S3_BUCKET --region eu-west-1 --create-bucket-configuration  LocationConstraint=eu-west-1

fi
