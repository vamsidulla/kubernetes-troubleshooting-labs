# Solution

The container listens on port `80`, while the readiness probe checks port `8080`. The container remains running, but the pod never becomes Ready. Kubernetes therefore excludes it from the Service's ready endpoints.

Apply the corrected manifest:

```bash
kubectl apply -n troubleshooting-labs -f fixed.yaml
kubectl rollout status -n troubleshooting-labs deployment/web-probe
kubectl get pods,endpoints -n troubleshooting-labs
```

The corrected probe references the named port `http`, reducing the chance of configuration drift between the container port, probe, and Service.

Prevention ideas:

- Prefer named ports across probes and Services.
- Test health endpoints as part of deployment validation.
- Monitor Ready replicas and endpoint counts separately from running pods.
