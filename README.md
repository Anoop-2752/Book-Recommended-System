# End-to-End-Book-Recommender-System

## Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py


![Image](https://github.com/user-attachments/assets/df891f91-60f9-4eb6-bd95-73ffb470bc0c)

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Anoop-2752/Book-Recommended-System
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now run,
```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t anoop/stapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 anoop/stapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push anoop/stapp:latest 
```

```bash
docker rmi anoop/stapp:latest
```

```bash
docker pull anoop/stapp
```
