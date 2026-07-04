import boto3

dynamodb = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:8147',
    region_name='us-west-2',
    aws_access_key_id='DUMMYIDEXAMPLE',
    aws_secret_access_key='DUMMYIDEXAMPLE'
)

PLAYER_ID = "a021c1e2-2528-464b-bc08-64e9b97824f0"  # Your player ID
UNLOCK_TO_ADD = "bounty_solvent"  # From your unlockableShopItems

# Add to shopUnlocks list
response = dynamodb.update_item(
    TableName='ThePit',
    Key={
        'playerId': {'S': PLAYER_ID}
    },
    UpdateExpression='SET shopUnlocks = list_append(if_not_exists(shopUnlocks, :empty), :unlock)',
    ExpressionAttributeValues={
        ':unlock': {'L': [{'S': UNLOCK_TO_ADD}]},
        ':empty': {'L': []}
    }
)

print(f"Added '{UNLOCK_TO_ADD}' to player {PLAYER_ID}")