# Komiser

[Komiser](https://komiser.io/) is an open sourced cloud environment inspector.

## Introduction

This chart bootstraps a Komiser instance community edition.

## Prerequisites

- Kubernetes 1.6+

## Configuration

**Enable service accounts to access AWS resources in three steps**

1. **[Create an IAM OIDC provider for your cluster](docs/enable-iam-roles-for-service-accounts.md)** – You only need to do this once for a cluster\.

2. **[Create an IAM role and attach an Komiser IAM policy to it with the permissions that your service accounts need](create-service-account-iam-policy-and-role.md)**

3. Update [templates/service-account.yaml](templates/service-account.yaml) with the IAM role you've created previously.

## Installing the chart

To install the chart:

```bash
$ helm install -f values.yaml komiser .
```

The above command deploys Komiser on the Kubernetes cluster in the default configuration.