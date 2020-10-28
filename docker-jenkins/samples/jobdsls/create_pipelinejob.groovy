import javaposse.jobdsl.dsl.DslFactory

DslFactory factory = this as DslFactory

factory.pipelineJob('pipeline_job_example') {
    definition {
        cpsScm {
            scriptPath("jenkins/Jenkinsfile.pipelinejob")
            scm {
                git {
                    // Specify the branches to examine for changes and to build.
                    // branch("*/master")
                    // Specify the branches to examine for changes and to build.
                    branches("*/master", "*/test")
                    // Adds a repository browser for browsing the details of changes in an external system.
                    browser {}
                    // Adds additional behaviors.
                    extensions {
                        cleanAfterCheckout()
                        cleanBeforeCheckout()
                        pruneBranches()
                        wipeOutWorkspace()
                    }
                    // Adds a remote.
                    remote {
                        // url("/tmp/samples/building-a-multibranch-pipeline-project")
                        url("https://github.com/i05nagai/building-a-multibranch-pipeline-project.git")
                    }
                }
            }
        }
    }

    description("pipeline description")

    displayName("pipeline displayname")

    logRotator {
        // If specified, artifacts from builds older than this number of days will be deleted, but the logs, history, reports, etc for the build will be kept.
        // artifactDaysToKeep(int artifactDaysToKeep)
        // If specified, only up to this number of builds have their artifacts retained.
        // artifactNumToKeep(int artifactNumToKeep)
        // If specified, build records are only kept up to this number of days.
        daysToKeep(10)
        // If specified, only up to this number of build records are kept.
        numToKeep(50)
    }
}
