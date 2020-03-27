pipeline {
  agent none
  stages {
    stage('Get Inputs') {
      agent none
      steps {
        script 
        {
            INPUTS = input message: 'User input required', ok: 'Provision Server!',
            parameters: [choice(name: 'Server_Type', choices: 'Windows\nLinux', description: 'What OS is the server we are provisioning?'),
            choice(name: 'Environment', choices: 'Dev\nQA\nqa-test\nProd', description: 'What is the environment Name?'),
            choice(name: 'NSX_tag1', choices: 'Choice1\nChoice2', description: 'What is the NSX tag for 1?'),
            choice(name: 'NSX_tag2', choices: 'Choice1\nChoice2', description: 'What is the NSX tag for 2?'),
            choice(name: 'NSX_tag3', choices: 'Choice1\nChoice2', description: 'What is the NSX tag for 3?'),
            choice(name: 'NSX_tag4', choices: 'Choice1\nChoice2', description: 'What is the NSX tag for 4?')
        ]
            
        }
        
        echo "ServerType: ${INPUTS['Server_Type']}"
      }
    }
    stage('Get Host Name') {
      agent {
        node('CentosTest02')
      }
      steps {
        label 'Get SCM'
        git poll: false, url: 'https://github.com/beakerman29/pipeline-with-feedback.git'
        script 
        {
            def output = sh encoding: 'UTF-8', label: 'Get host name', returnStdout: true, script: "${WORKSPACE}"+'/Hostname.py --atestinput set'
            env.HOSTNAME = output.split(',')[0]
            env.PASSMEON = output.split(',')[1]
            
            
        }
        echo "${env.HOSTNAME}"
        echo "${env.PASSMEON}"
        echo "${INPUTS['Server_Type']}"
      }
    }
    stage('Get IP') {
        agent {
            node('CentosTest')
        }
        steps
        {
            label 'Get SCM'
            git poll: false, url: 'https://github.com/beakerman29/pipeline-with-feedback.git'
            script 
            {
                def output = sh encoding: 'UTF-8', label: 'Get host name', returnStdout: true, script: "${WORKSPACE}"+'/Hostname.py --atestinput '+"${env.PASSMEON}"
                env.HOSTNAME2 = output.split(',')[0]
                env.PASSMEON2 = output.split(',')[1]
                
            }
            echo "${env.HOSTNAME}"
            echo "${env.HOSTNAME2}"
            echo "${env.PASSMEON2}"
        }
    }
}
}