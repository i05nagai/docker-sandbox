

## Directory strcture

- home
    - Kibana home directory or `$KIBANA_HOME`
    - `/usr/share/kibana`
- bin
    - Binary scripts including kibana to start the Kibana server and kibana-plugin to install plugins
    - `/usr/share/kibana/bin`
- config
    - Configuration files including kibana.yml
    - /etc/kibana
- data
    - The location of the data files written to disk by Kibana and its plugins
    - /var/lib/kibana
    - path.data
- optimize
    - Transpiled source code. Certain administrative actions (e.g. plugin install) result in the source code being retranspiled on the fly.
    - /usr/share/kibana/optimize
- plugins
    - Plugin files location. Each plugin will be contained in a subdirectory.
    - /usr/share/kibana/plugins


## Reference
- [Install Kibana with Debian Package \| Kibana User Guide \[7\.2\] \| Elastic](https://www.elastic.co/guide/en/kibana/current/deb.html)
- [elastic/kibana\-docker: Official Kibana Docker image](https://github.com/elastic/kibana-docker)
