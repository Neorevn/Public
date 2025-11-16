# RSVP App

This application is a simple RSVP web app that uses a MongoDB backend.

## Deployment

The application is deployed to Kubernetes. The manifest files can be found in the `frontend/` and `backend/` directories.

### Prerequisites

Before deploying, you must create a Kubernetes secret to hold the MongoDB credentials.

1.  Create a file named `secrets.yml` in the `RSVPApp` root directory. This file is ignored by git.

2.  Add the following content to `secrets.yml`, replacing the placeholder values with your actual MongoDB credentials:

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

3.  Apply the secret to your Kubernetes cluster:
    ```bash
    kubectl apply -f secrets.yml
    ```

After creating the secret, you can proceed with deploying the rest of the application components.