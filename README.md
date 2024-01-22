# EndToEnd_MLProject_With_CiCd-Docker

## Boston House Pricing Prediction

#### **Data description:-**


`The Boston data frame has 506 rows and 14 columns.`

`This data frame contains the following columns:`

1. `crim` -
per capita crime rate by town.

2. `zn` -
proportion of residential land zoned for lots over 25,000 sq.ft.

3. `indus` -
proportion of non-retail business acres per town.

4. `chas` -
Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).

5. `nox` -
nitrogen oxides concentration (parts per 10 million).

6. `rm` -
average number of rooms per dwelling.

7. `age` -
proportion of owner-occupied units built prior to 1940.

8. `dis` -
weighted mean of distances to five Boston employment centres.

9. `rad` -
index of accessibility to radial highways.

10. `tax` -
full-value property-tax rate per $10,000.

11. `ptratio` -
pupil-teacher ratio by town.

12. `black` -
1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.

13. `stat` -
lower status of the population (percent).

14. `medv` -
median value of owner-occupied homes in $1000s.




#### **Software And Tools Requirements**

1. Github Account
2. HerokuAccount
3. VSCodeIDE
4. GitCLI

**Create a new environment**
``Python3 -m venv env_name``


### End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml --- data type of all columns
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/SubramanyaNayak-github/EndToEnd_MLProject_With_CiCd-Docker

```
### STEP 01- Create a conda environment after opening the repository

```bash
python3 -m venv mlproj
```

```bash

source mlproj/bin/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/subramanyanayak3/EndToEnd_MLProject_With_CiCd-Docker.mlflow \
MLFLOW_TRACKING_USERNAME=subramanyanayak3 \
MLFLOW_TRACKING_PASSWORD=b18ad68cf0c678f5f616a47081e6c4c129e4a844 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/subramanyanayak3/EndToEnd_MLProject_With_CiCd-Docker.mlflow

export MLFLOW_TRACKING_USERNAME=subramanyanayak3 

export MLFLOW_TRACKING_PASSWORD=b18ad68cf0c678f5f616a47081e6c4c129e4a844

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 380675867318.dkr.ecr.eu-north-1.amazonaws.com/boston

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


