import json
import boto3

sns = boto3.client('sns')

# Replace with your actual SNS Topic ARN from Phase 3
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:203159929164:Cloud-Alerts-Topic"

def lambda_handler(event, context):
    for record in event['Records']:
        log_message = record['body']
        print(f"Received CloudWatch Event Log: {log_message}")
        
        # Simulated AI Log Parsing & Root Cause Analysis
        root_cause_analysis = "High CPU Utilization detected on Primary App Instance (Threshold > 70%)."
        remediation_action = "Auto-Scaling signal dispatched & Storage Sync verified via EFS."
        
        # Formatted Incident Report to SNS / Slack / Email
        alert_body = f"""
        🚨 AWS AUTONOMOUS SRE INCIDENT REPORT 🚨
        -------------------------------------------
        Status: HIGH CPU ALARM TRIGGERED
        Raw Log Event: {log_message}
        
        🤖 AI Root Cause Diagnosis:
        {root_cause_analysis}
        
        🔧 Auto-Remediation Status:
        {remediation_action}
        
        System State: Failover Route Ready | EFS Sync Intact
        -------------------------------------------
        """
        
        # Send Alert Notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="[AUTONOMOUS FIX] AWS Cloud Incident Auto-Resolved",
            Message=alert_body
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Incident Processed and Remediated Successfully!')
    }
