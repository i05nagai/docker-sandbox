
## Overview



```
./docker_run.sh
```

Then access to `http://localhost:8080`.
You need to enter the password which is displaied on your log.

## Syntax
- [Pipeline Syntax](https://jenkins.io/doc/book/pipeline/syntax/)
    - docker
- parameter
    - [Pipeline Syntax](https://jenkins.io/doc/book/pipeline/syntax/#parameters-example)
- script
    - [Pipeline Syntax](https://jenkins.io/doc/book/pipeline/syntax/#script)

- list of steps
    - [Pipeline Steps Reference](https://jenkins.io/doc/pipeline/steps/)

## Tutorial
* [jenkins\-docs/building\-a\-multibranch\-pipeline\-project: For an advanced tutorial on how to use Jenkins to build a multibranch Pipeline project with selectively executed stages\.](https://github.com/jenkins-docs/building-a-multibranch-pipeline-project)

```
cd samples
git clone https://github.com/jenkins-docs/building-a-multibranch-pipeline-project.git
cd building-a-multibranch-pipeline-project
git branch development
git branch production
```

- Access to `https://localhost:8080`.
- Enable docker-plugin
    - Go to `Manage Jenkins`
    - Go to `Manage Pluigns`
    - Go to `Available` page and Install `Docker` plugin
        - Plugin id is `docker-plugin`
- Click `Ceate new job`.
- Choose multibranch pipelione projecft with name `sample-multibranch`
- Access to `https://localhost:8080/restart`.
    - There is a bug of folder plugin which cause endless loading
- Go to configure on `sample-multibranch` project 
- Fill out configure
    - Branch sources
        - Git
        - Project Repository: `/tmp/samples/building-a-multibranch-pipeline-project`
        - credentials: none
        - Property strategy: `All branhces get the same properties`
- `Scan Multibranch Pipeline Now`
- Override the `Jenkinsfile` on master branch

```
pipeline {
    agent {
        docker {
            image 'node:6-alpine'
            args '-p 3000:3000 -p 5000:5000' 
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh './jenkins/scripts/test.sh'
            }
        }
    }
}
```


- Then commit the change
    - `git stage .`
    - `git commit -m "Add initial Jenkinsfile with 'Test' stage"`
- Go to `msater` branch on `sample-multibranch` project
- Click `Build Now` on left pane

```
pipeline {
    agent {
        docker {
            image 'node:6-alpine'
            args '-p 3000:3000 -p 5000:5000'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh './jenkins/scripts/test.sh'
            }
        }
        stage('Deliver for development') {
            when {
                branch 'development' 
            }
            steps {
                sh './jenkins/scripts/deliver-for-development.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh './jenkins/scripts/kill.sh'
            }
        }
        stage('Deploy for production') {
            when {
                branch 'production'  
            }
            steps {
                sh './jenkins/scripts/deploy-for-production.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh './jenkins/scripts/kill.sh'
            }
        }
    }
}
```


#### Error
[\[JENKINS\-55310\] Folders plugin blocks job creation \- Jenkins JIRA](https://issues.jenkins-ci.org/browse/JENKINS-55310?page=com.atlassian.jira.plugin.system.issuetabpanels%3Achangehistory-tabpanel)

If I restart the instance (via http://localhost:8080/restart), the issue disappear and I'm able to create any job and I'm even able to edit it (The error 500 has disappear as well)

#### Plugins
- pipeline-utility-steps
    - https://jenkins.io/doc/pipeline/steps/pipeline-utility-steps/

## Reference
* https://github.com/jenkinsci/docker
* [Getting started with the Guided Tour](https://jenkins.io/doc/pipeline/tour/getting-started/)
* [End\-to\-End Multibranch Pipeline Project Creation](https://jenkins.io/doc/tutorials/build-a-multibranch-pipeline-project/)
- https://jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#sh-shell-script
