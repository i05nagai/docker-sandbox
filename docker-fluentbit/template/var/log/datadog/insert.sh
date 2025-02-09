#!/bin/bash

echo "2024-11-02 07:07:52 UTC | CORE | ERROR | (comp/aggregator/demultiplexer/demultiplexerimpl/demultiplexer.go:74 in newDemultiplexer) | Error while getting hostname, exiting: unable to reliably determine the host name. You can define one in the agent config file or in your hosts file" >> agent.log
echo "2024-11-02 07:08:52.658776513 process-agent exited with code 0, disabling" >> init.log
echo "2024-11-02 07:08:52 UTC | PROCESS | INFO | (command/main_common.go:283 in runApp) | The process-agent has successfully been shut down" >> process-agent.log
echo "2024-11-02 07:07:49 UTC | SECURITY | INFO | (pkg/config/setup/config.go:1938 in LoadCustom) | Starting to load the configuration" >> security-agent.log
echo "2024-11-02 07:07:53 UTC | SYS-PROBE | INFO | (pkg/config/remote/client/client.go:423 in pollLoop) | retrying the first update of remote-config state (could not acquire agent auth token: unable to read authentication token file: open /etc/datadog-agent/auth_token: no such file or directory)" >> system-probe.log
