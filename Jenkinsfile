node {
    def main

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       main = docker.build("emilyswitz/devops-repository")
    }

    stage('Test image') {
  

        main.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            main.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
