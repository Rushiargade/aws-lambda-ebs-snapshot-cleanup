import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    VOLUME_ID = "vol-0abc1234def567890"  # 🔁 replace with your volume ID
    RETENTION_MINUTES = 5  # For testing

    # ---------------- CREATE SNAPSHOT ----------------
    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Automated snapshot created by Lambda"
    )

    snapshot_id = snapshot['SnapshotId']
    print(f"Created snapshot: {snapshot_id}")

    # ---------------- CLEANUP OLD SNAPSHOTS ----------------
    cutoff_time = datetime.now(timezone.utc) - timedelta(minutes=RETENTION_MINUTES)

    snapshots = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [VOLUME_ID]}
        ],
        OwnerIds=['self']
    )['Snapshots']

    deleted_snapshots = []

    for snap in snapshots:
        start_time = snap['StartTime']
        if start_time < cutoff_time:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            deleted_snapshots.append(snap['SnapshotId'])

    if deleted_snapshots:
        print("Deleted snapshots:")
        for s in deleted_snapshots:
            print(s)
    else:
        print("No snapshots older than 5 minutes found")

    return {
        "statusCode": 200,
        "body": "EBS snapshot creation and cleanup completed"
    }
