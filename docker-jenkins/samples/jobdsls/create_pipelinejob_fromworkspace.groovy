import javaposse.jobdsl.dsl.DslFactory

DslFactory factory = this as DslFactory

factory.pipelineJob('pipelinejob_from_workspace') {
    // definition of pipeline job
    definition {
        cps {
            script(readFileFromWorkspace('create_pipelinejob_fromworkspace.groovy'))
            sandbox()
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

