# prefect-demo

1. Pipeline generator
    - flow --> pipeline
    - task --> unit of work
    - pure Python, no need for XComs
1. Orion UI
    ```
    prefect orion start
    ```
1. Deployments
    - a flow that you want to trigger from UI and set on a schedule
    - "API representations of flows and allow for their remote configuration and scheduling"
    - make a deployment with CLI (`prefect deployment`) or programmatically with Python
1. Agents and pools
    - agents are the "workers" that run your flows
    - separate Python process that runs in the background
    - agents are split by pools
    - each pool can have queues
1. Blocks
    - "blocks securely store credentials and configuration to easily manage connections to external systems"
    - can be created in UI or programmatically
1. Infrastructure and Storage for Deployments
    - deployment can have infrastructure and storage
    - infrastructure is the "compute environment" where your flow runs
        - docker, kubernetes, etc.
        - Lambda-s, Google Cloud Run
    - storage is the "location where your flow is stored"
        - Github
        - S3, GCS
