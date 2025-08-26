pipeline{
    agent any
        stages {
            stage ("Create Selenum Grid container"){
                steps {
                    sh "docker compose -f docker-compose-selgrid.yaml up -d"
                }
            }
            stage ("Run Tests on container"){
                steps {
                    sh "docker build -t pytestsel ."
                    sh "mkdir -p outputs"
                    sh "docker run -v ./outputs:/home/Project/page_obj_proj/outputs pytestsel >> outputs/pytest.out.log"                    
                }
            }

        }
        post {
            always {
                sh "docker compose -f docker-compose-selgrid.yaml down"
                archiveArtifacts artifacts: 'outputs/**', followSymlinks: false
                sh "docker system prune -af"
            }
        }
}
  