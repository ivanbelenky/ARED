#! /bin/sh
wget -O ARED0.tar.gz https://ared0.s3.amazonaws.com/ARED0.tar.gz
wget -O ARED0.csv https://ared0.s3.amazonaws.com/ARED0.csv
tar -xvf ARED0.tar.gz -C .
mv dataset/ARED0.csv dataset/ARED0.csv
rm ARED0.tar.gz