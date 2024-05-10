pipeline {
    agent any
    environment {
        GIT_BRANCH='main'
        GITHUB_URL='https://github.com/nikitajalkote/simple_flask_repo.git'
        EC2_DIR='/home/ubuntu'
        FLASK_SCRIPT='my_flask.py'
        SSH_KEY='server2_ID'
        EC2_USER='ubuntu'
        EC2_HOST='3.138.137.23'
    }

    stages {
        stage('Flask Deployment') {
            steps {
                echo 'This is Flask application'
            }
        }
        stage('checkout'){
            steps {
                git branch: env.GIT_BRANCH, url: env.GITHUB_URL
            }
        }
        stage('Connect Ec2'){
            steps {
                 sshagent(credentials: ['server2_ID']){
                     sh '''
                       ssh -o StrictHostKeyChecking=no ubuntu@3.138.137.23 '
                      
                       pwd
                       ls
                       
                       '
                     '''
                }
            }
        }
        stage('copy file from local'){
            steps {
                sshagent(credentials: ['server2_ID']) {
                    sh '''
                    scp -o StrictHostKeyChecking=no -r ${WORKSPACE}/* ubuntu@3.138.137.23:/home/ubuntu/
                    '''
                }
            }
        } 
        stage('Run Python Application'){
            steps {
                 sshagent(credentials: ['server2_ID']){
                     sh '''
                       ssh -o StrictHostKeyChecking=no ubuntu@3.138.137.23 '
                       sudo apt update -y
                       sudo apt install python3 -y
                      
                       sudo cp my_flask.py /var/www/html

                       python3 ${FLASK_SCRIPT}
                       '
                     '''
                }
            }  
        }
        
    }
}    
