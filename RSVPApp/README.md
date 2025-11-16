# RSVP Management Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

A simple, containerized web application for managing event RSVPs, deployed on Kubernetes. This project demonstrates a basic microservices pattern with a Python/Flask frontend and a MongoDB database, orchestrated by Kubernetes.

## 📸 Screenshot

*(To add a screenshot, take a picture of the running application and place it here. You can drag and drop the image into the GitHub editor.)*

<p align="center">
  <img width="800" alt="Application Screenshot Placeholder" src="https://user-images.githubusercontent.com/10633355/189851153-1b8a2363-7344-46ec-9f33-64997f8f4f78.png" />
</p>

---

## 🏛️ Architecture

This application is designed to run on Kubernetes and is composed of two main services:

-   **Frontend (Flask)**: A Python Flask web server that renders the user interface and handles user interactions. It connects to the MongoDB backend to store and retrieve RSVP data.
-   **Database (MongoDB)**: A MongoDB instance that persists all RSVP information.

Both components are deployed as containerized workloads on a Kubernetes cluster, communicating with each other over the internal cluster network.

---

## 📂 Project Structure

The repository is organized by service, with Kubernetes manifests defining each component.

```
RSVPApp/
├── db/
│   ├── deployment.yml
│   ├── secrets.yml
│   └── service.yml
├── frontend/
│   ├── deployment.yml
│   └── service.yml
└── README.md
```

---

## 🛠️ Tech Stack

-   **Backend:** Python, Flask
-   **Database:** MongoDB
-   **Containerization:** Docker
-   **Orchestration:** Kubernetes
-   **Local Development:** Minikube

---

## 🚀 Getting Started

Follow these instructions to deploy and run the RSVP application on a local Kubernetes cluster using Minikube.

### Prerequisites

-   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
-   [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed.
-   [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed.

### 1. Start Your Kubernetes Cluster

Open your terminal and start Minikube. This will create a single-node Kubernetes cluster inside Docker.

```sh
minikube start
```

### 2. Create the Application Namespace

All resources for this app will be isolated in their own namespace for better organization.

```sh
kubectl create namespace rsvp-app
```

### 3. Deploy the Application

Apply the Kubernetes manifest files to create the database and frontend components. Run these commands from the root of the `RSVPApp` directory.

```sh
# Deploy the MongoDB database and its service
kubectl apply -f db/

# Deploy the Flask frontend and its service
kubectl apply -f frontend/
```

### 4. Verify the Deployment

Check that all the pods are up and running. It may take a minute for the containers to be pulled and started. You should see all pods with a `STATUS` of `Running` and `READY` as `1/1`.

```sh
kubectl get pods -n rsvp-app
```

**Example Output:**
```
NAME                       READY   STATUS    RESTARTS   AGE
mongodb-66bcfb6946-wfqlw   1/1     Running   0          2m
rsvp-5b7bd9cb58-9wdc6      1/1     Running   0          90s
rsvp-5b7bd9cb58-w5fxf      1/1     Running   0          90s
```

### 5. Access the Application

Because Minikube runs in an isolated Docker network, you cannot directly access the application using the node's IP address from your browser.

The easiest way to access the service is to use the built-in `minikube service` command. This command creates a secure tunnel from your local machine to the service inside the cluster and opens the correct URL in your browser.

```sh
minikube service rsvp -n rsvp-app
```

This will automatically open the RSVP application in your default web browser.

> **Note:** You must keep the terminal where you ran `minikube service` open. Closing it will terminate the connection to the application.

### 🧹 Cleaning Up

To stop the application and delete all its resources, run the following commands:

```sh
# Delete the application resources from the cluster
kubectl delete namespace rsvp-app

# Stop the local Kubernetes cluster
minikube stop
```