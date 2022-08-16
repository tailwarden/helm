1. Grab the **OpenID Connect provider URL** from the **ADMIN** account.

2. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the left navigation pane, choose **Identity Providers** under **Access management**\.

1. To create a provider, choose **Add Provider**\.

1. For **Provider Type**, choose **OpenID Connect**\.

1. For **Provider URL**, paste the ADMIN OIDC issuer URL, and then choose **Get thumbprint**\.

1. For **Audience**, enter `sts.amazonaws.com` and choose **Add provider**\.