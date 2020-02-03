#!/bin/sh
S3_BUCKET=rommoviestorage
if [[ $(aws s3api list-buckets --query 'Buckets[?starts_with(Name,`rommoviestorage`)].[Name]' --output text) = 'rommoviestorage' ]]
then  
    echo "Bucket $S3_BUCKET already exists"; 
else
   echo "About to create $S3_BUCKET"
   aws s3api create-bucket --bucket $S3_BUCKET --region eu-west-1 --create-bucket-configuration  LocationConstraint=eu-west-1

fi
aws s3 cp ../src/web/static/images s3://$S3_BUCKET/images --recursive