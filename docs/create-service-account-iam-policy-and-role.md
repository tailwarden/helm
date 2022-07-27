1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the left navigation pane, choose **Policies** and then choose **Create policy**\. 

1. Choose the **JSON** tab\.

1. In the **Policy Document** field, paste the Komiser recommended [policy](https://github.com/mlabouardy/komiser/blob/master/policy.json).

1. Choose **Review policy**\.

1. Enter a name and description for your policy and then choose **Create policy**\.

1. Record the Amazon Resource Name \(ARN\) of the policy to use later when you create your role\.

## Create an IAM role for a service account<a name="create-service-account-iam-role"></a>

1. Copy the following code block to your computer.

   ```
   read -r -d '' TRUST_RELATIONSHIP <<EOF
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::${ACCOUNT_ID}:oidc-provider/${OIDC_PROVIDER}"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "${OIDC_PROVIDER}:aud": "sts.amazonaws.com",
             "${OIDC_PROVIDER}:sub": "system:serviceaccount:${NAMESPACE}:komiser"
           }
         }
       }
     ]
   }
   EOF
   echo "${TRUST_RELATIONSHIP}" > trust.json
   ```

`NOTE: Make sure to substitute ${NAMESPACE} for the namespace you will deploy the helm chart in. If deployed in any other namespace, you will see sts:AssumeRoleWithWebIdentity failure messages in the pod logs.`

1. Run the modified code block from the previous step to create a file named *`trust.json`*\.

1. Run the following AWS CLI command to create the role\. Replace `my-iam-role` with a name for your IAM role, and `my-role-description` with a description for your role\.

   ```
   aws iam create-role --role-name my-iam-role --assume-role-policy-document file://trust.json --description "my-role-description"
   ```

1. Run the following command to attach an IAM policy to your role\. Replace `my-iam-role` with the name of your IAM role, `111122223333` with your account ID \(or with **aws**, if you're attaching an AWS managed policy\), and `my-iam-policy` with the name of an existing policy that you created or an IAM AWS managed policy\.

   ```
   aws iam attach-role-policy --role-name my-iam-role --policy-arn=arn:aws:iam::111122223333:policy/my-iam-policy
   ```
