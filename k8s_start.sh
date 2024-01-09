cd k8s/

kubectl apply -f deployment-front-web.yaml
kubectl apply -f deployment-redis.yaml
kubectl apply -f service-redis.yaml
kubectl apply -f service-front-web.yaml


cd ..