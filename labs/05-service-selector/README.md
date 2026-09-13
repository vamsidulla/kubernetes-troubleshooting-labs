# Lab 05: Service has no ready endpoints

Run commands from the repository root in a disposable learning cluster. These examples do not require cloud resources.

## Set up

```bash
kubectl config current-context
kubectl create namespace troubleshooting-labs --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n troubleshooting-labs -f labs/05-service-selector/broken.yaml
```

Observe the failure before applying the fix. Image downloads and restart backoff can take time.

## Investigate

```bash
kubectl get pods -n troubleshooting-labs -l app=service-selector-lab --show-labels
kubectl get svc service-selector-lab -n troubleshooting-labs -o yaml
kubectl get endpointslices -n troubleshooting-labs -l kubernetes.io/service-name=service-selector-lab -o yaml
kubectl exec -n troubleshooting-labs deployment/service-selector-lab -- wget -T 3 -qO- http://127.0.0.1:8080/
kubectl exec -n troubleshooting-labs deployment/service-selector-lab -- wget -T 3 -qO- http://service-selector-lab/
```

## Expected evidence

The Pod should become Ready and localhost should return `healthy`. The Service selector matches no Pods, so EndpointSlices have no ready backend addresses (or none exist). The Service request fails.

## Explain your diagnosis

A shop is open, but the directory lists a different address. Which Kubernetes objects represent the shop and directory?

<details>
<summary>Reveal root cause, fix, and interview answer</summary>

The Service selects `app=wrong-selector`, but the Pod has `app=service-selector-lab`. Correct the selector. Prevention: reuse label definitions in templates and verify Service connectivity after deployments.

```bash
kubectl apply -n troubleshooting-labs -f labs/05-service-selector/fixed.yaml
kubectl rollout status -n troubleshooting-labs deployment/service-selector-lab --timeout=120s
```

The Pod is the shop; the Service selector determines its backend directory. After applying the fix, repeat the EndpointSlice and Service wget commands. Expect a ready address and `healthy`. A successful rollout alone does not prove a Service works.

</details>

## Cleanup and repeat

```bash
kubectl delete -n troubleshooting-labs -f labs/05-service-selector/fixed.yaml --ignore-not-found
```

Delete these lab resources before repeating the broken setup. Do not apply the entire labs directory recursively: broken and fixed files deliberately define the same objects.

## Validation status

Manifests were parsed and checked for consistent references. Expected runtime evidence is instructional; no cluster execution results are claimed.
