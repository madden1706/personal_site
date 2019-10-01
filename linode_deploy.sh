curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# need root pass
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update
sudo apt-get install -y docker-ce

#docker without sudo
sudo usermod -aG docker ${USER}
su - ${USER}
# id -nG # check addition

# pull git repo.
# build images/
# docker-compose up -f prodfile.