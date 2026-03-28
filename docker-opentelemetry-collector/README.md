


```
go install github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen@latest
```

## CLI

```
telemetrygen traces
```

- `--batch`
    Whether to batch traces (default true)
- `--ca-cert string`
    - Trusted Certificate Authority to verify server certificate
- `--child-spans int`
    - Number of child spans to generate for each trace (default 1)
- `--client-cert string`
    - Client certificate file
- `--client-key string`
    - Client private key file
- `--duration duration`
    - For how long to run the test
- `--interval duration`
    - Reporting interval (default 1s)
- `--marshal`
    - Whether to marshal trace context via HTTP headers
- `--mtls`
    - Whether to require client authentication for mTLS
- `--otlp-attributes map[string]any`
    - Custom telemetry attributes to use. The value is expected in one of the following formats: key="value", key=true, key=false, or key=<integer>. Note you may need to escape the quotes when using the tool from a cli. Flag may be repeated to set multiple attributes (e.g --otlp-attributes key1=\"value1\" --otlp-attributes key2=\"value2\" --telemetry-attributes key3=true --telemetry-attributes key4=123)
- `--otlp-endpoint string`
    - Destination endpoint for exporting logs, metrics and traces
- `--otlp-header map[string]any`
    - Custom header to be passed along with each OTLP request. The value is expected in the format key="value". Note you may need to escape the quotes when using the tool from a cli. Flag may be repeated to set multiple headers (e.g --otlp-header key1=\"value1\" --otlp-header key2=\"value2\")
- `--otlp-http`
    - Whether to use HTTP exporter rather than a gRPC one
--otlp-http-url-path string             Which URL path to write to (default "/v1/traces")
- `--otlp-insecure`
    - Whether to enable client transport security for the exporter's grpc or http connection
- `--otlp-insecure-skip-verify`
    - Whether a client verifies the server's certificate chain and host name
- `--rate float`
    - Approximately how many metrics/spans/logs per second each worker should generate. Zero means no throttling.
- `--service string`
    - Service name to use (default "telemetrygen")
- `--size int`
    - Desired minimum size in MB of string data for each trace generated. This can be used to test traces with large payloads, i.e. when testing the OTLP receiver endpoint max receive size.
- `--span-duration duration`
    - The duration of each generated span. (default 123µs)
- `--status-code string`
    - Status code to use for the spans, one of (Unset, Error, Ok) or the equivalent integer (0,1,2) (default "0")
- `--telemetry-attributes map[string]any`
    - Custom telemetry attributes to use. The value is expected in one of the following formats: key="value", key=true, key=false, or key=<integer>. Note you may need to escape the quotes when using the tool from a cli. Flag may be repeated to set multiple attributes (e.g --telemetry-attributes key1=\"value1\" --telemetry-attributes key2=\"value2\" --telemetry-attributes key3=true --telemetry-attributes key4=123)
- `--traces int`
    - Number of traces to generate in each worker (ignored if duration is provided) (default 1)
- `--workers int`
    - Number of workers (goroutines) to run (default 1)

```
$ telemetrygen traces --otlp-insecure --traces 3

2025-08-11T18:13:53.745+0900    INFO    traces/traces.go:52     starting gRPC exporter
2025-08-11T18:13:53.746+0900    INFO    grpclog/component.go:69 [core] original dial target is: "localhost:4317"        {"grpc_log": true}
2025-08-11T18:13:53.747+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel created      {"grpc_log": true}
2025-08-11T18:13:53.747+0900    INFO    channelz/trace.go:200   [core] [Channel #1]parsed dial target is: resolver.Target{URL:url.URL{Scheme:"dns", Opaque:"", User:(*url.Userinfo)(nil), Host:"", Path:"/localhost:4317", RawPath:"", OmitHost:false, ForceQuery:false, RawQuery:"", Fragment:"", RawFragment:""}}    {"grpc_log": true}
2025-08-11T18:13:53.748+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel authority set to "localhost:4317"    {"grpc_log": true}
2025-08-11T18:13:53.748+0900    INFO    traces/traces.go:116    generation of traces isn't being throttled
2025-08-11T18:13:53.749+0900    INFO    traces/worker.go:112    traces generated        {"worker": 0, "traces": 3}
2025-08-11T18:13:53.749+0900    INFO    traces/traces.go:74     stop the batch span processor
2025-08-11T18:13:53.750+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel exiting idle mode    {"grpc_log": true}
2025-08-11T18:13:53.772+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Resolver state updated: {
  "Addresses": [
    {
      "Addr": "[::1]:4317",
      "ServerName": "",
      "Attributes": null,
      "BalancerAttributes": null,
      "Metadata": null
    },
    {
      "Addr": "127.0.0.1:4317",
      "ServerName": "",
      "Attributes": null,
      "BalancerAttributes": null,
      "Metadata": null
    }
  ],
  "Endpoints": [
    {
      "Addresses": [
        {
          "Addr": "[::1]:4317",
          "ServerName": "",
          "Attributes": null,
          "BalancerAttributes": null,
          "Metadata": null
        }
      ],
      "Attributes": null
    },
    {
      "Addresses": [
        {
          "Addr": "127.0.0.1:4317",
          "ServerName": "",
          "Attributes": null,
          "BalancerAttributes": null,
          "Metadata": null
        }
      ],
      "Attributes": null
    }
  ],
  "ServiceConfig": null,
  "Attributes": null
} (resolver returned new addresses)     {"grpc_log": true}
2025-08-11T18:13:53.772+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel switches to new LB policy "pick_first"       {"grpc_log": true}
2025-08-11T18:13:53.772+0900    INFO    grpclog/prefix_logger.go:42     [pick-first-leaf-lb] [pick-first-leaf-lb 0x140001cc3f0] Received new config {
  "shuffleAddressList": false
}, resolver state {
  "Addresses": [
    {
      "Addr": "[::1]:4317",
      "ServerName": "",
      "Attributes": null,
      "BalancerAttributes": null,
      "Metadata": null
    },
    {
      "Addr": "127.0.0.1:4317",
      "ServerName": "",
      "Attributes": null,
      "BalancerAttributes": null,
      "Metadata": null
    }
  ],
  "Endpoints": [
    {
      "Addresses": [
        {
          "Addr": "[::1]:4317",
          "ServerName": "",
          "Attributes": null,
          "BalancerAttributes": null,
          "Metadata": null
        }
      ],
      "Attributes": null
    },
    {
      "Addresses": [
        {
          "Addr": "127.0.0.1:4317",
          "ServerName": "",
          "Attributes": null,
          "BalancerAttributes": null,
          "Metadata": null
        }
      ],
      "Attributes": null
    }
  ],
  "ServiceConfig": null,
  "Attributes": null
}       {"grpc_log": true}
2025-08-11T18:13:53.773+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel Connectivity change to CONNECTING    {"grpc_log": true}
2025-08-11T18:13:53.773+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #2]Subchannel created     {"grpc_log": true}
2025-08-11T18:13:53.773+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #2]Subchannel Connectivity change to CONNECTING   {"grpc_log": true}
2025-08-11T18:13:53.773+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #2]Subchannel picks a new address "[::1]:4317" to connect {"grpc_log": true}
2025-08-11T18:13:53.773+0900    INFO    grpclog/component.go:69 [core] Creating new client transport to "{Addr: \"[::1]:4317\", ServerName: \"localhost:4317\", }": connection error: desc = "transport: Error while dialing: dial tcp [::1]:4317: connect: connection refused"        {"grpc_log": true}
2025-08-11T18:13:53.773+0900    WARN    channelz/trace.go:202   [core] [Channel #1 SubChannel #2]grpc: addrConn.createTransport failed to connect to {Addr: "[::1]:4317", ServerName: "localhost:4317", }. Err: connection error: desc = "transport: Error while dialing: dial tcp [::1]:4317: connect: connection refused"    {"grpc_log": true}
google.golang.org/grpc/internal/channelz.AddTraceEvent
        /Users/makoto.nagai/.asdf/installs/golang/1.23.7/packages/pkg/mod/google.golang.org/grpc@v1.74.2/internal/channelz/trace.go:202
google.golang.org/grpc/internal/channelz.Warningf
        /Users/makoto.nagai/.asdf/installs/golang/1.23.7/packages/pkg/mod/google.golang.org/grpc@v1.74.2/internal/channelz/logging.go:55
google.golang.org/grpc.(*addrConn).createTransport
        /Users/makoto.nagai/.asdf/installs/golang/1.23.7/packages/pkg/mod/google.golang.org/grpc@v1.74.2/clientconn.go:1414
google.golang.org/grpc.(*addrConn).tryAllAddrs
        /Users/makoto.nagai/.asdf/installs/golang/1.23.7/packages/pkg/mod/google.golang.org/grpc@v1.74.2/clientconn.go:1354
google.golang.org/grpc.(*addrConn).resetTransportAndUnlock
        /Users/makoto.nagai/.asdf/installs/golang/1.23.7/packages/pkg/mod/google.golang.org/grpc@v1.74.2/clientconn.go:1286
google.golang.org/grpc.(*addrConn).connect
        /Users/makoto.nagai/.asdf/installs/golang/1.23.7/packages/pkg/mod/google.golang.org/grpc@v1.74.2/clientconn.go:942
2025-08-11T18:13:53.774+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #2]Subchannel Connectivity change to TRANSIENT_FAILURE, last error: connection error: desc = "transport: Error while dialing: dial tcp [::1]:4317: connect: connection refused"  {"grpc_log": true}
2025-08-11T18:13:53.774+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #3]Subchannel created     {"grpc_log": true}
2025-08-11T18:13:53.774+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #3]Subchannel Connectivity change to CONNECTING   {"grpc_log": true}
2025-08-11T18:13:53.774+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #3]Subchannel picks a new address "127.0.0.1:4317" to connect     {"grpc_log": true}
2025-08-11T18:13:53.778+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #3]Subchannel Connectivity change to READY        {"grpc_log": true}
2025-08-11T18:13:53.778+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #2]Subchannel Connectivity change to SHUTDOWN     {"grpc_log": true}
2025-08-11T18:13:53.778+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #2]Subchannel deleted     {"grpc_log": true}
2025-08-11T18:13:53.778+0900    INFO    grpclog/prefix_logger.go:42     [pick-first-leaf-lb] [pick-first-leaf-lb 0x140001cc3f0] SubConn 0x14000146500 reported connectivity state READY and the health listener is disabled. Transitioning SubConn to READY.   {"grpc_log": true}
2025-08-11T18:13:53.778+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel Connectivity change to READY {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel Connectivity change to SHUTDOWN      {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Closing the name resolver    {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    channelz/trace.go:200   [core] [Channel #1]ccBalancerWrapper: closing   {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #3]Subchannel Connectivity change to SHUTDOWN     {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    channelz/trace.go:200   [core] [Channel #1 SubChannel #3]Subchannel deleted     {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    grpclog/prefix_logger.go:42     [transport] [client-transport 0x1400029a908] Closing: rpc error: code = Canceled desc = grpc: the client connection is closing  {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    grpclog/prefix_logger.go:42     [transport] [client-transport 0x1400029a908] loopyWriter exiting with error: rpc error: code = Canceled desc = grpc: the client connection is closing  {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    channelz/trace.go:200   [core] [Channel #1]Channel deleted      {"grpc_log": true}
2025-08-11T18:13:53.782+0900    INFO    traces/traces.go:64     stopping the exporter
```


### Metrics


```
telemetrygen metrics
```

```
telemetrygen logs
```


