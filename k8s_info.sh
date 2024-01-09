echo -e "---> Deployments:"
kubectl get deployments

echo -e "\n---> Servicios:"
kubectl get services

echo -e "\n---> Pods:"
kubectl get pods

echo -e "\n---> Volúmenes persistentes:"
kubectl get pv

echo -e "\n---> Reclamaciones de volúmenes persistentes:"
kubectl get pvc
