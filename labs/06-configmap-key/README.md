# Lab 06: CreateContainerConfigError from a missing key

Run commands from the repository root in a disposable learning cluster. These examples do not require cloud resources.

## Set up

```bash
kubectl config current-context
kubectl create namespace troubleshooting-labs --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n troubleshooting-labs -f labs/06-configmap-key/broken.yaml
```

Observe the failure before applying the fix. Image downloads and restart backoff can take time.

## Investigate

```bash
kubectl get pods -n troubleshooting-labs -l app=config-key-lab
kubectl describe pods -n troubleshooting-labs -l app=config-key-lab
kubectl get configmap config-key-settings -n troubleshooting-labs -o yaml
kubectl get deployment config-key-lab -n troubleshooting-labs -o yaml
```

## Expected evidence

The ConfigMap exists, but its required `APP_MODE` key does not. Events should report the missing key and the container waits with `CreateContainerConfigError`. If pulling the image fails first, resolve that prerequisite before diagnosing the key.

## Explain your diagnosis

How does this differ from Lab 01, where the application exits because configuration is missing?

<details>
<summary>Reveal root cause, fix, and interview answer</summary>

The environment reference is required by default. Add the missing key. Kubelet retries container creation; allow time for the ConfigMap update to propagate. Prevention: validate key references and namespace alignment before rollout.

```bash
kubectl apply -n troubleshooting-labs -f labs/06-configmap-key/fixed.yaml
kubectl rollout status -n troubleshooting-labs deployment/config-key-lab --timeout=120s
```

Here Kubernetes cannot construct the container configuration, so the process has not started. In Lab 01 the process started and exited. Once Ready, verify with `kubectl exec -n troubleshooting-labs deployment/config-key-lab -- printenv APP_MODE`. Expect `learning`. Existing running containers do not automatically refresh ConfigMap environment variables; this case works because startup had been blocked.

</details>

## Cleanup and repeat

```bash
kubectl delete -n troubleshooting-labs -f labs/06-configmap-key/fixed.yaml --ignore-not-found
```

Delete these lab resources before repeating the broken setup. Do not apply the entire labs directory recursively: broken and fixed files deliberately define the same objects.

## Validation status

Manifests were parsed and checked for consistent references. Expected runtime evidence is instructional; no cluster execution results are claimed.
