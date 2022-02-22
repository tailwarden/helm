# Komiser

[Komiser](https://komiser.io/) is an open sourced cloud environment inspector.

## Introduction

This chart bootstraps a Komiser instance community edition.

## Prerequisites

- Kubernetes 1.6+

## Installing the chart

To install the chart:

```bash
$ helm install .
```

The above command deploys Komiser on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

The chart is customized for AWS usage and using `iam-role`.

## Uninstalling the chart

To uninstall/delete the deployment:

```bash
$ helm list
NAME       	REVISION	UPDATED                 	STATUS  	CHART          	NAMESPACE
kindly-newt	1       	Mon Oct  2 15:05:44 2017	DEPLOYED	komiser-2.5.0	  default
$ helm delete kindly-newt
```

## Configuration

The following table lists the configurable parameters of the Komiser chart and their default values.

| Parameter               | Description                              | Default                    |
| ----------------------- | ---------------------------------------- | -------------------------- |
| `replicaCount`          | Number of replicas deployed              | `1`                        |
| `role`                  | IAM Role ARN value                       | `""`                       |
| `image.repository`      | image repository                         | `sonarqube`                |
| `image.tag`             | `komiser` image tag.                     | `2.5.0`                    |
| `image.pullPolicy`      | Image pull policy                        | `IfNotPresent`             |
| `ingress.enabled`       | Flag for enabling ingress                | false                      |
| `ingress.annotations`   | Ingress additional annotations           | `{}`                       |
| `ingress.hosts[0].name` | Hostname to your Komiser installation    | `komiser.organization.com` |
| `ingress.path`          | Path where to mound the URL structure    | /                          |
| `ingress.tls`           | Ingress secrets for TLS certificates     | `[]`                       |
| `service.type`          | Kubernetes service type                  | `ClusterIP`                |
| `service.port`          | Service port                             | 3000                       |
| `resources`             | Sonarqube Pod resource requests & limits | `{}`                       |
| `affinity`              | Node / Pod affinities                    | `{}`                       |

For overriding variables see: [Customizing the chart](https://docs.helm.sh/using_helm/#customizing-the-chart-before-installing)
