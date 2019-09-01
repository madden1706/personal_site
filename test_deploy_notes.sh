# Congifure profile for ECS command line.

ecs-cli configure --cluster madresearchden-test --default-launch-type EC2 --config-name madresearchden-test --region eu-west-2
ecs-cli configure profile --access-key  --secret-key  --profile-name madresearchden_test

# Cluster creation -  this is using the mrd-test profile. (User is madresearchden_test )
# need to make sure that the user has the sufficient priveleges to create the resources needed.
# Key pair needs to be for the EC instance. Ensure that it is the correct key. It is the name of the key on the instane... that it will use? 

ecs-cli up --keypair Administrator-key-pair-London --capability-iam --size 1 --instance-type t2.micro --cluster-config madresearchden-test --ecs-profile madresearchden-test
# What if I want two instances of of difference sizes?? 


# Need to ensure that the instance has enough memory with reference to the ecs-compose.yml
# The compose files are sensitive to white space.
# Also sensitive to other docker commands e.g. volumes
ecs-cli compose up --create-log-groups --cluster-config madresearchden-test --ecs-profile madresearchden-test

# Test the status.
ecs-cli ps --cluster-config madresearchden-test --ecs-profile madresearchden-test
ecs-cli compose down --cluster-config madresearchden-test --ecs-profile madresearchden-test

# Serive to live.
ecs-cli compose service up --cluster-config madresearchden-test --ecs-profile madresearchden-test

#Clean up
# Stop containers
ecs-cli compose service rm --cluster-config madresearchden-test --ecs-profile madresearchden-test
# Shut down cluster
ecs-cli down --force --cluster-config madresearchden-test --ecs-profile madresearchden-test