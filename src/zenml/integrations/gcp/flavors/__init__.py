#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""GCP integration flavors."""

from zenml.integrations.gcp.flavors.gcp_artifact_store_flavor import (
    GCPArtifactStoreConfig,
    GCPArtifactStoreFlavor,
)
from zenml.integrations.gcp.flavors.gcp_secrets_manager_flavor import (
    GCPSecretsManagerConfig,
    GCPSecretsManagerFlavor,
)
from zenml.integrations.gcp.flavors.vertex_orchestrator_flavor import (
    VertexOrchestratorConfig,
    VertexOrchestratorFlavor,
)
from zenml.integrations.gcp.flavors.vertex_step_operator_flavor import (
    VertexStepOperatorConfig,
    VertexStepOperatorFlavor,
)

from zenml.integrations.gcp.flavors.gcp_vm_orchestrator_flavor import (
    GcpVMOrchestratorConfig,
    GcpVMOrchestratorFlavor,
)

__all__ = [
    "GCPArtifactStoreFlavor",
    "GCPArtifactStoreConfig",
    "GCPSecretsManagerFlavor",
    "GCPSecretsManagerConfig",
    "VertexOrchestratorFlavor",
    "VertexOrchestratorConfig",
    "VertexStepOperatorFlavor",
    "VertexStepOperatorConfig",
    "GcpVMOrchestratorConfig",
    "GcpVMOrchestratorFlavor",
]
