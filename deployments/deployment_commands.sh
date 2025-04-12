#apply deployment and services
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# verify running pods
kubectl get pods

#get service info
kubectl get svc fastapi-service

#apply ingress(optional)
kubectl apply -f ingress.yaml


#docker build command
docker build -t fastapi-video-analysis .

#docker repo push 
docker push dockersmnt/fastapi-video-analysis:latest

#docker image pull
docker pull dockersmnt/fastapi-video-analysis:latest

#container running
docker run -p 8000:8000 dockersmnt/fastapi-video-analysis
