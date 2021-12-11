# In the container

# Check Linux distro
cat /etc/os-release

# Check Python version
python -V

# Install dependencies
python -m pip install -r ~/src/recommendations/requirements.txt
python -m pip install -r ~/src/marketplace/requirements.txt

# Generate Python code from the protobufs
cd ~/src/recommendations
python -m grpc_tools.protoc -I ../protobufs \
    --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto

# Run the gRPC server
python ~/scr/recommendations/recommendations.py

# Run the main Flask app (and create protobufs code)
cd ~/src/marketplace
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
    --grpc_python_out=. ../protobufs/recommendations.proto

FLASK_APP=marketplace.py flask run

# Containerize microservices / run in WSL host
cd src

docker build . -f recommendations/Dockerfile -t recommendations
docker run -p 127.0.0.1:50051:50051/tcp recommendations
CTRL+C

docker build . -f marketplace/Dockerfile -t marketplace
docker run -p 127.0.0.1:5000:5000/tcp marketplace
CTRL+C

# -- NETWORKING

# Define virtual network
docker network create microservices
docker run -p 127.0.0.1:50051:50051/tcp --network microservices \
    --name recommendations recommendations

docker build . -f marketplace/Dockerfile -t marketplace
docker run -p 127.0.0.1:5000:5000/tcp \
    --network microservices \
    -e RECOMMENDATIONS_HOST=recommendations marketplace

# -- DOCKER COMPOSE
cd src
docker-compose build
docker-compose up

# Execute integration tests on microservices inside marketplace container
docker-compose exec marketplace pytest marketplace_integration_test.py


# -- KUBERNETES
3 To deploy Docker images to a cloud provider, you need to push your Docker images 
# to an image registry like Docker Hub.
minikube start
kubectl apply -f kubernetes.yaml

kubectl get pods
kubectl get service marketplace
#kubectl port-forward deployment/marketplace :5000
kubectl port-forward deployment/marketplace 5000:5000

