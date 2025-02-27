# Table of contents

## Getting Started

* [Introduction](./getting-started/introduction.md)
* [Core Concepts](./getting-started/core-concepts.md)
* [Installation](./getting-started/installation/installation.md)
  * [Installation on M1 Macs](./getting-started/installation/m1-mac-installation.md)
* [Quickstart](https://github.com/zenml-io/zenml/tree/main/examples/quickstart)
* [Deploying ZenML](./getting-started/deploying-zenml/deploying-zenml.md)
  * [One Click Deployment using CLI](./getting-started/deploying-zenml/cli.md)
  * [Deploying with Docker](./getting-started/deploying-zenml/docker.md)
  * [Deploying with Helm](./getting-started/deploying-zenml/helm.md)
* [Examples](./getting-started/examples.md)

## Starter Guide

* [Pipelines](./starter-guide/pipelines/pipelines.md)
  * [Fetching Pipelines](./starter-guide/pipelines/fetching-pipelines.md)
  * [Step Parameterization and Caching](./starter-guide/pipelines/iterating.md)
* [Stacks](./starter-guide/stacks/stacks.md)
  * [Registering Stacks](./starter-guide/stacks/registering-stacks.md)
  * [Managing Stacks](./starter-guide/stacks/managing-stacks.md)
* [Collaboration](./starter-guide/collaborate/collaborate.md)
  * [Connecting to a Deployed ZenML](./starter-guide/collaborate/zenml-deployment.md)
  * [Inviting Users](./starter-guide/collaborate/users.md)

## Advanced Guide

* [In-depth Configuration](./advanced-guide/pipelines/pipelines.md)
  * [Runtime Settings](./advanced-guide/pipelines/settings.md)
  * [Containerization (Docker)](./advanced-guide/pipelines/containerization.md)
  * [Passing Custom Data Types through Steps (Materializers)](./advanced-guide/pipelines/materializers.md)
  * [Specifying Step Resources](./advanced-guide/pipelines/step-resources.md)
  * [Enabling GPU-backed hardware](./advanced-guide/pipelines/gpu-hardware.md)
  * [Accessing Metadata within Steps](./advanced-guide/pipelines/step-metadata.md)
  * [Controlling the Step Execution Order](./advanced-guide/pipelines/step-order.md)
* [Extending Stacks](./advanced-guide/stacks/stacks.md)
  * [Writing Custom Flavors](./advanced-guide/stacks/custom-flavors.md)
  * [Managing Stack Component States](./advanced-guide/stacks/stack-state-management.md)
  * [Managing External Services](./advanced-guide/stacks/manage-external-services.md)
* [Practical MLOps](./advanced-guide/practical/practical-mlops.md)
  * [Stack Recipes](./advanced-guide/practical/stack-recipes.md)
  * [Switching Orchestration](./advanced-guide/practical/switching-orchestration.md)
  * [Secrets Management](./advanced-guide/practical/secrets-management.md)
  * [Tracking Experiments](./advanced-guide/practical/tracking-experiments.md)
  * [Validating Data](./advanced-guide/practical/validating-data.md)
  * [Deploying Models and Batch Inference](./advanced-guide/practical/deploying-models.md)

## Component Gallery

* [Categories of MLOps Tools](./component-gallery/categories.md)
* [Integration Overview](./component-gallery/integrations.md)
* [Orchestrators](./component-gallery/orchestrators/orchestrators.md)
  * [Local Orchestrator](./component-gallery/orchestrators/local.md)
  * [Local Docker Orchestrator](./component-gallery/orchestrators/local-docker.md)
  * [Kubeflow Orchestrator](./component-gallery/orchestrators/kubeflow.md)
  * [Kubernetes Orchestrator](./component-gallery/orchestrators/kubernetes.md)
  * [Google Cloud VertexAI Orchestrator](./component-gallery/orchestrators/gcloud-vertexai.md)
  * [Tekton Orchestrator](./component-gallery/orchestrators/tekton.md)
  * [GitHub Actions Orchestrator](./component-gallery/orchestrators/github-actions.md)
  * [Airflow Orchestrator](./component-gallery/orchestrators/airflow.md)
  * [Develop a Custom Orchestrator](./component-gallery/orchestrators/custom.md)
* [Artifact Stores](./component-gallery/artifact-stores/artifact-stores.md)
  * [Local Artifact Store](./component-gallery/artifact-stores/local.md)
  * [Amazon Simple Cloud Storage (S3)](./component-gallery/artifact-stores/amazon-s3.md)
  * [Google Cloud Storage (GCS)](./component-gallery/artifact-stores/gcloud-gcs.md)
  * [Azure Blob Storage](./component-gallery/artifact-stores/azure-blob-storage.md)
  * [Develop a Custom Artifact Store](./component-gallery/artifact-stores/custom.md)
* [Container Registries](./component-gallery/container-registries/container-registries.md)
  * [Default Container Registry](./component-gallery/container-registries/default.md)
  * [DockerHub](./component-gallery/container-registries/dockerhub.md)
  * [Amazon Elastic Container Registry (ECR)](./component-gallery/container-registries/amazon-ecr.md)
  * [Google Cloud Container Registry](./component-gallery/container-registries/gcloud.md)
  * [Azure Container Registry](./component-gallery/container-registries/azure.md)
  * [GitHub Container Registry](./component-gallery/container-registries/github.md)
  * [Develop a Custom Container Registry](./component-gallery/container-registries/custom.md)
* [Secrets Managers](./component-gallery/secrets-managers/secrets-managers.md)
  * [Local Secrets Manager](./component-gallery/secrets-managers/local.md)
  * [AWS Secrets Manager](./component-gallery/secrets-managers/aws.md)
  * [Google Cloud Secrets Manager](./component-gallery/secrets-managers/gcp.md)
  * [Azure Secrets Manager](./component-gallery/secrets-managers/azure.md)
  * [GitHub Secrets Manager](./component-gallery/secrets-managers/github.md)
  * [HashiCorp Vault Secrets Manager](./component-gallery/secrets-managers/hashicorp-vault.md)
  * [Develop a Custom Secrets Manager](./component-gallery/secrets-managers/custom.md)
* [Data Validators](component-gallery/data-validators/data-validators.md)
  * [Great Expectations](component-gallery/data-validators/great-expectations.md)
  * [Deepchecks](component-gallery/data-validators/deepchecks.md)
  * [Evidently](component-gallery/data-validators/evidently.md)
  * [Whylogs](component-gallery/data-validators/whylogs.md)
  * [Develop a Custom Data Validator](component-gallery/data-validators/custom.md)
* [Experiment Trackers](./component-gallery/experiment-trackers/experiment-trackers.md)
  * [MLflow](./component-gallery/experiment-trackers/mlflow.md)
  * [Weights & Biases](./component-gallery/experiment-trackers/wandb.md)
  * [Develop a Custom Experiment Tracker](./component-gallery/experiment-trackers/custom.md)
* [Model Deployers](./component-gallery/model-deployers/model-deployers.md)
  * [MLflow](./component-gallery/model-deployers/mlflow.md)
  * [Seldon](./component-gallery/model-deployers/seldon.md)
  * [KServe](./component-gallery/model-deployers/kserve.md)
  * [Develop a Custom Model Deployer](./component-gallery/model-deployers/custom.md)
* [Step Operators](./component-gallery/step-operators/step-operators.md)
  * [Amazon SageMaker](./component-gallery/step-operators/amazon-sagemaker.md)
  * [Google Cloud VertexAI](./component-gallery/step-operators/gcloud-vertexai.md)
  * [AzureML](./component-gallery/step-operators/azureml.md)
  * [Spark](./component-gallery/step-operators/spark.md)
  * [Develop a Custom Step Operator](./component-gallery/step-operators/custom.md)
* [Alerters](./component-gallery/alerters/alerters.md)
  * [Slack Alerter](./component-gallery/alerters/slack.md)
  * [Develop a Custom Alerter](./component-gallery/alerters/custom.md)
* [Feature Stores](./component-gallery/feature-stores/feature-stores.md)
  * [Feast](./component-gallery/feature-stores/feast.md)
  * [Develop a Custom Feature Store](./component-gallery/feature-stores/custom.md)
* [Annotators](./component-gallery/annotators/annotators.md)
  * [Label Studio](./component-gallery/annotators/label-studio.md)
  * [Develop a Custom Annotator](./component-gallery/annotators/custom.md)

## Guidelines

* [Best Practices](guidelines/best-practices.md)
* [Global Configuration](guidelines/global-config.md)
* [System Environmental Variables](guidelines/system-environmental-variables.md)
* [Migration Guide 0.20.0](guidelines/migration-zero-twenty.md)

## Misc

* [Contribution Guide](misc/contributing.md)
* [External Integration Guide](misc/integrating.md)
* [Usage Analytics](misc/usage-analytics.md)

## Reference

* [Community & Content](reference/community-and-content.md)
* [Glossary](reference/glossary.md)
* [FAQ](reference/faq.md)
* [CLI Cheat Sheet](reference/cheat-sheet.md)
* [CLI Reference](https://apidocs.zenml.io/latest/cli/)
* [API Reference](https://apidocs.zenml.io/latest/)
