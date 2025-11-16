# RSVP App

This application is a simple RSVP web app built with a React frontend, a Python backend, and a MongoDB database. It is designed to be deployed on Kubernetes.

## Prerequisites

Before you begin, ensure you have the following tools installed:

*   **Git**: To clone the repository.
*   **kubectl**: The Kubernetes command-line tool.
*   **A Kubernetes Cluster**: You can use one of the following options.

    ### Option 1: Minikube (For users without Docker Desktop)

    [Minikube](httpss://minikube.sigs.k8s.io/docs/start/) is a great tool for running a single-node Kubernetes cluster locally.

    1.  Install Minikube and a hypervisor driver (like VirtualBox or Hyper-V).
    2.  Start your cluster:
        ```bash
        minikube start
        ```

    ### Option 2: Docker Desktop

    If you have [Docker Desktop](httpss://www.docker.com/products/docker-desktop/), you can enable its built-in Kubernetes cluster.

    1.  Go to `Settings` > `Kubernetes`.
    2.  Check `Enable Kubernetes`.
    3.  Click `Apply & Restart`.

## Deployment

Follow these steps to deploy the entire application stack to your Kubernetes cluster.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd RSVPApp
```

### 2. Create the Namespace

All components will be deployed into the `rsvp-app` namespace.

```bash
kubectl create namespace rsvp-app
```

### 3. Create the MongoDB Secret

The application requires credentials to connect to MongoDB. You must create a `secrets.yml` file for this.

1.  Create a file named `secrets.yml` in the root `RSVPApp` directory. This file is intentionally ignored by Git to keep your credentials safe.

2.  Add the following content to `secrets.yml`, replacing the placeholder values with your MongoDB credentials.

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: mongodb-secret
      namespace: rsvp-app
    type: Opaque
    stringData:
      MONGODB_USER: "your-mongodb-user"
      MONGODB_PASSWORD: "your-mongodb-password"
    ```

3.  Apply the secret to your cluster:
    ```bash
    kubectl apply -f secrets.yml
    ```

### 4. Deploy MongoDB

Deploy the MongoDB stateful set and its service.

```bash
kubectl apply -f db/mongo-statefulset.yml -n rsvp-app
```

### 5. Deploy the RSVP Application

Deploy the backend and frontend components of the RSVP application.

```bash
kubectl apply -f backend/ -n rsvp-app
kubectl apply -f frontend/ -n rsvp-app
```

## Accessing the Application

Once all pods are running, you can access the application.

*   **For Minikube users:**
    The easiest way to access the service is to run:
    ```bash
    minikube service rsvp -n rsvp-app
    ```
    This command will open the application in your default web browser.

*   **For Docker Desktop and other users:**
    The service is exposed as a `NodePort`. Find the port by running:
    ```bash
    kubectl get svc rsvp -n rsvp-app
    ```
    You can then access the application at `http://localhost:<node-port>`.

## Cleanup

To remove all the application components from your cluster, run the following command:

```bash
kubectl delete namespace rsvp-app
```