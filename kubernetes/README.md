For this demo purpose, I will deploy this Dockerized web app in `Kubernetes` using `LoadBalancer` service in a `minikube` K8s cluster. In production environment, we mostly use `Ingress` that exposes HTTP and HTTPS routes from outside the K8s cluster to services within the cluster.
 
In a `minikube` cluster, the following resources will be deployed for this sample stateless Python Flask application.

![k8s-lb](https://user-images.githubusercontent.com/116319959/236712593-4d4063b4-7c97-4cc7-b310-3a5bae76abae.png)
