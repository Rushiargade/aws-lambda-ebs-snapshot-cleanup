# Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

## 📌 Objective
The objective of this project is to automate the backup process of Amazon EBS volumes by creating regular snapshots and deleting old snapshots based on a defined retention period. This helps ensure data protection while optimizing storage costs.

For testing purposes, the snapshot retention period is set to **5 minutes** instead of 30 days.

---

## 🛠 AWS Services Used
- Amazon EC2 (EBS)
- AWS Lambda
- AWS IAM
- Amazon EventBridge (CloudWatch Events)
- Amazon CloudWatch Logs
- Boto3 (AWS SDK for Python)

---

## 💾 EBS Volume Details
- A specific EBS volume is selected for backup.
- The Lambda function creates snapshots for the specified volume automatically.

---

## 🧾 IAM Role & Permissions
The Lambda function uses an IAM role with the following policies:
- `AmazonEC2FullAccess`
- `AWSLambdaBasicExecutionRole`

> Note: In production environments, permissions should be restricted following the principle of least privilege.

---

## 🧠 Lambda Function Workflow
1. Initialize the EC2 client using Boto3
2. Create a snapshot for the specified EBS volume
3. List all snapshots related to the volume
4. Delete snapshots older than the defined retention period
5. Log snapshot creation and deletion details to CloudWatch

---

## 🧪 Testing Procedure
1. Identify an existing EBS volume
2. Manually invoke the Lambda function
3. Verify a new snapshot is created
4. Wait for more than **5 minutes**
5. Invoke the Lambda function again
6. Confirm that snapshots older than 5 minutes are deleted

---

## 📊 Logging & Monitoring
- Lambda execution logs are available in **Amazon CloudWatch Logs**
- Logs show:
  - Snapshot IDs created
  - Snapshot IDs deleted
  - Execution status messages

---

## 📅 Automation (Bonus)
- The Lambda function can be scheduled using **Amazon EventBridge**
- Example: Weekly snapshot creation using a cron schedule

---

## ✅ Result
After execution:
- A snapshot is created for the selected EBS volume
- Old snapshots beyond the retention period are automatically deleted
- Backup automation and cost optimization are achieved

---
