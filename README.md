# Kubernetes Troubleshooting Labs

Hands-on failure scenarios for practicing Kubernetes diagnosis with a repeatable **observe → hypothesize → test → fix → prevent** workflow.

## Why this repository exists

Production Kubernetes work is less about memorizing commands and more about connecting symptoms across events, pod state, logs, probes, networking, and application behavior. Each lab starts with a deliberate failure and includes:

- A reproducible manifest
- Investigation commands
- Expected evidence
- Root-cause explanation
- Corrective and preventive actions

## AKS troubleshooting atlas

The [AKS Troubleshooting Atlas](aks-troubleshooting/) adds 30 Azure-specific runbooks across beginner, intermediate, and advanced levels. It covers access, identity, networking, DNS, storage, node health, autoscaling, upgrades, private clusters, large-cluster control-plane pressure, and Istio. Each runbook starts with evidence, groups common causes, gives a resolution path, defines verification, and links to primary documentation.

## Current coverage

The repository has two complementary formats: **7 runnable exercises** in `labs/` and **30 completed diagnostic runbooks** in the [atlas coverage matrix](aks-troubleshooting/COVERAGE.md). A completed runbook does not imply that a standalone broken/fixed lab exists.

| Area previously listed on the roadmap | Completed coverage | Standalone exercise status |
|---|---|---|
| Private registry authentication | [B03: image pulls](aks-troubleshooting/beginner/b03-image-pull.md), [I01: ACR identity, secrets, and network access](aks-troubleshooting/intermediate/i01-acr-auth-network.md) | Lab 04 covers invalid tags; authentication exercise remains to be built |
| Service targetPort mismatch | [B07: selectors, readiness, targetPort, and protocol](aks-troubleshooting/beginner/b07-service-endpoints.md) | Lab 05 covers selectors; targetPort exercise remains to be built |
| DNS and NetworkPolicy | [B08: DNS resolution](aks-troubleshooting/beginner/b08-dns-resolution.md), [I04: NetworkPolicy/NSG](aks-troubleshooting/intermediate/i04-networkpolicy-nsg.md) | Standalone exercises remain to be built |
| PVC scheduling and mount failures | [B09: PVC Pending](aks-troubleshooting/beginner/b09-pvc-pending.md), [A05: Azure Disk topology](aks-troubleshooting/advanced/a05-azure-disk-topology.md), [A06: Azure Files mounts](aks-troubleshooting/advanced/a06-azure-files.md) | Standalone exercises remain to be built |
| Requests, limits, OOMKilled, and node pressure | [B06: scheduling](aks-troubleshooting/beginner/b06-pod-pending.md), [I07: node pressure](aks-troubleshooting/intermediate/i07-node-notready-pressure.md), [I08: OOM, throttling, eviction](aks-troubleshooting/intermediate/i08-resource-saturation.md) | Lab 07 covers node selectors; resource-pressure exercises remain to be built |
| Ingress and Gateway API routing | [I03: Ingress/TLS](aks-troubleshooting/intermediate/i03-ingress-routing-tls.md), [A10: managed Istio ingress](aks-troubleshooting/advanced/a10-istio-ingress.md) | Ingress is documented; A10 mentions Gateway API inspection, but dedicated Gateway API conditions/reference troubleshooting and runnable exercises remain gaps |

## Labs

| Lab | Scenario | Skills demonstrated |
|---|---|---|
| [01](labs/01-crashloopbackoff/) | Container repeatedly restarts because required configuration is missing | Pod status, events, logs, exit codes, ConfigMaps |
| [02](labs/02-readiness-probe/) | Application runs but never becomes Ready because the probe targets the wrong port | Probes, endpoints, Services, in-pod testing |
| [03](labs/03-competing-consumers/) | Queue events appear intermittent because two service instances compete for messages | Messaging semantics, replica discovery, hypothesis-driven troubleshooting |
| [04](labs/04-imagepullbackoff/) | ImagePullBackOff from an invalid tag | Investigation, correction, verification |
| [05](labs/05-service-selector/) | Service has no ready endpoints | Investigation, correction, verification |
| [06](labs/06-configmap-key/) | CreateContainerConfigError from a missing key | Investigation, correction, verification |
| [07](labs/07-node-selector/) | Pending Pod from unmatched node selection | Investigation, correction, verification |

## Prerequisites

- A local Kubernetes cluster such as Minikube, kind, or Docker Desktop
- `kubectl`
- Bash-compatible terminal

Verify access:

```bash
kubectl cluster-info
kubectl get nodes
```

## Run a lab

```bash
kubectl create namespace troubleshooting-labs
kubectl apply -n troubleshooting-labs -f labs/01-crashloopbackoff/broken.yaml
```

Start with the investigation guide inside the lab directory before opening `solution.md`.

Clean up safely:

```bash
kubectl delete namespace troubleshooting-labs
```

## Core diagnostic workflow

```bash
kubectl get pods -n troubleshooting-labs -o wide
kubectl describe pod -n troubleshooting-labs <pod-name>
kubectl logs -n troubleshooting-labs <pod-name>
kubectl logs -n troubleshooting-labs <pod-name> --previous
kubectl get events -n troubleshooting-labs --sort-by=.metadata.creationTimestamp
```

## Safety

All examples use an isolated namespace and intentionally broken resources. Run them only in a personal learning cluster, never in a shared or production environment.

## Roadmap

The topics in **Current coverage** are delivered as runbooks. Remaining work is to turn documented scenarios into repeatable exercises and add a dedicated Gateway API diagnostic path.

### Next lab 08: DNS egress blocked by NetworkPolicy (proposed)

- **Scope:** In an isolated namespace, apply default-deny egress to a diagnostic client while keeping an explicitly allowed backend reachable by IP. Omit the DNS allowance so Service-name lookups fail. Inspect policy selectors and pod resolver settings, then add narrowly scoped UDP/TCP 53 access to the cluster's actual DNS endpoint. Keep unrelated egress denied. This exercises the existing B08/I04 guidance rather than adding a new incident family.
- **Prerequisites:** A disposable cluster with a CNI that enforces NetworkPolicy, `kubectl`, and a client image with DNS and HTTP tools. Identify CoreDNS labels/namespace and whether NodeLocal DNSCache changes the resolver path; adapt the DNS allowance to that cluster. Verify enforcement with a denied control request before starting.
- **Validation:** Before the fix, the allowed backend succeeds by IP but fails by Service name, and an unrelated destination remains blocked. After the fix, UDP and TCP DNS queries and the same Service-name HTTP request succeed; the unrelated destination remains blocked. Capture policy/resolver evidence and results before and after, then remove the lab namespace.

### Next lab 09: Gateway API cross-namespace backend reference (proposed)

- **Scope:** Create a Gateway and HTTPRoute in a frontend namespace and a healthy Service in a backend namespace. Use a cross-namespace backendRef without a ReferenceGrant. Diagnose the route's `ResolvedRefs=False` condition and its reason, then add a ReferenceGrant in the backend namespace limited to that frontend namespace, HTTPRoute kind, and named Service. Keep route attachment valid so this isolates reference authorization from listener or targetPort failures. Add a companion Gateway API runbook linking I03/A10.
- **Prerequisites:** A disposable cluster with compatible Gateway API CRDs, a running Gateway API controller that supports HTTPRoute and cross-namespace Service references, an accepted GatewayClass, and a reachable Gateway listener (local forwarding is sufficient). Confirm the backend responds directly and the route's parent/listener permits attachment before injecting the reference failure.
- **Validation:** Before the fix, the backend is healthy but the route reports `ResolvedRefs=False` with a reference-denial reason and the Gateway request cannot reach it. After the scoped grant, the route reports `Accepted=True` and `ResolvedRefs=True` for the intended controller/parent at the current generation, the Gateway is `Programmed=True`, and a request with the configured Host/path returns the backend's expected response. Remove the grant to reproduce denial, then clean up both namespaces and any lab-owned cluster-scoped resources.

Each proposed exercise should include `broken.yaml`, investigation instructions with expected evidence, a documented fix/solution, validation commands, and cleanup instructions. These proposals are not implemented labs.

After these two labs, add standalone registry-authentication, targetPort, PVC, resource-pressure, and Ingress exercises using the existing runbooks as the diagnostic references.

## Author

Created by [Vamsi Krishna](https://github.com/vamsidulla) as part of a practical Cloud DevOps/SRE portfolio.
