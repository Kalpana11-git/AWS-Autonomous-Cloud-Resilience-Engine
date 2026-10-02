# 🚀 Autonomous AWS Cloud Resilience, Auto-Remediation & FinOps Engine

An enterprise-grade, event-driven SRE automation platform built on AWS that detects infrastructure anomalies, buffers system logs during traffic bursts, executes auto-healing, and dispatches real-time incident diagnosis reports.

---

## 🏗️ Architecture & Network Setup
- *Networking:* Custom Multi-AZ VPC (10.0.0.0/16) provisioned across us-east-1a and us-east-1b using Public and Private Subnets with Internet Gateway routing.
- *Compute & Storage:* EC2 Instances hosted inside secure Private Subnets integrated with AWS Elastic File System (EFS) for persistent data synchronization.
- *Monitoring & Telemetry:* CloudWatch metric alarms monitoring CPU utilization and infrastructure health.
- *Event-Driven Buffering:* AWS SQS queue decoupling system telemetry to eliminate event loss during spike loads.
- *Automated Remediation Engine:* AWS Lambda (Python Boto3) consuming SQS events to run auto-healing logic and sending root-cause analysis via AWS SNS.

---

## 🛠️ AWS Services & Tech Stack
- *Cloud Provider:* Amazon Web Services (AWS)
- *Core Services:* VPC, Subnets, EC2, EFS, CloudWatch, SQS, SNS, Lambda, IAM, S3
- *Language & SDK:* Python 3.12, AWS Boto3 SDK
- *Architecture Pattern:* Event-Driven Microservices / Automated Cloud SRE

---

## 📋 System Workflow
1. *Detection:* CloudWatch monitors EC2 CPU utilization and triggers an alarm when thresholds (>70%) are breached.
2. *Buffering:* Alarm payloads are pushed asynchronously into an AWS SQS queue.
3. *Processing:* AWS Lambda triggers automatically upon receiving messages from the SQS queue.
4. *Remediation & Alerting:* Python script evaluates the log trace, simulates auto-remediation, and dispatches a structured incident report to engineers via AWS SNS.

---

## 📄 License
This project is open-source and available under the MIT License.
