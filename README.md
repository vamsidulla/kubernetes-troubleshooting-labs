# Kubernetes Troubleshooting Labs

Hands-on failure scenarios for practicing Kubernetes diagnosis with a repeatable **observe → hypothesize → test → fix → prevent** workflow.

## Why this repository exists

Production Kubernetes work is less about memorizing commands and more about connecting symptoms across events, pod state, logs, probes, networking, and application behavior. Each lab starts with a deliberate failure and includes:

- A reproducible manifest
- Investigation commands
- Expected evidence
- Root-cause explanation
- Corrective and preventive actions

## Labs

| Lab | Scenario | Skills demonstrated |
|---|---|---|
| [01](labs/01-crashloopbackoff/) | Container repeatedly restarts because required configuration is missing | Pod status, events, logs, exit codes, ConfigMaps |
| [02](labs/02-readiness-probe/) | Application runs but never becomes Ready because the probe targets the wrong port | Probes, endpoints, Services, in-pod testing |
| [03](labs/03-competing-consumers/) | Queue events appear intermittent because two service instances compete for messages | Messaging semantics, replica discovery, hypothesis-driven troubleshooting |

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

- ImagePullBackOff and registry authentication
- Service selector and endpoint failures
- DNS and NetworkPolicy troubleshooting
- PVC scheduling and mount failures
- CPU/memory requests, limits, and OOMKilled
- Ingress and Gateway API routing

## Author

Created by [Vamsi Krishna](https://github.com/vamsidulla) as part of a practical Cloud DevOps/SRE portfolio.
