# Solution

The container exits with code `1` because `APP_MODE` is not defined. Kubernetes restarts the failed container and eventually applies an increasing backoff delay, producing `CrashLoopBackOff`.

Evidence:

- `kubectl logs` shows `ERROR: APP_MODE is required`.
- `kubectl describe pod` shows the terminated state and exit code.
- The restart count increases over time.
- `kubectl logs --previous` retrieves output from the preceding container instance.

Apply the correction:

```bash
kubectl apply -n troubleshooting-labs -f fixed.yaml
kubectl rollout status -n troubleshooting-labs deployment/config-checker
```

Prevention ideas:

- Validate required configuration during CI/CD.
- Use admission policies or Helm schema validation.
- Emit explicit startup errors rather than failing silently.
- Alert on restart-rate changes, not only current pod phase.
