#!/bin/bash

cd kubernetes

kubectl apply -f postgres-deployment.yml
kubectl apply -f postgres-service.yml
kubectl apply -f redis-deployment.yml
kubectl apply -f redis-service.yml
kubectl apply -f django-deployment.yml
kubectl apply -f django-service.yml