# Lab 01: CrashLoopBackOff from missing configuration

## Objective

Determine why a container starts, exits, and is repeatedly restarted by Kubernetes.

## Deploy the failure

```bash
kubectl apply -n troubleshooting-labs -f broken.yaml
kubectl get pods -n troubleshooting-labs -w
```

## Investigation tasks

1. Identify the pod state and restart count.
2. Review pod events.
3. Read current and previous container logs.
4. Determine the process exit code.
5. Identify the missing runtime dependency.

Useful commands:

```bash
kubectl get pods -n troubleshooting-labs
kubectl describe pod -n troubleshooting-labs -l app=config-checker
kubectl logs -n troubleshooting-labs -l app=config-checker
kubectl logs -n troubleshooting-labs -l app=config-checker --previous
```

When you have a root-cause hypothesis, compare it with [solution.md](solution.md).
