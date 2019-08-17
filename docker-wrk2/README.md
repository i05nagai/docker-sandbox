## CLI

```
wrk <option> <url>
```

* `-c, --connections <N>`
    * Connections to keep open
* `-d, --duration <T>`
    * Duration of test
* `-t, --threads <N>`
    * Number of threads to use
* `-s, --script <S>`
    * Load Lua script file
* `-H, --header <H>`
    * Add header to request
* `-L  --latency`
    * Print latency statistics
* `-U  --u_latency`
    * Print uncorrected latency statistics
* `--timeout <T>`
    * Socket/request timeout
* `-B, --batch_latency`
    * Measure latency of whole batches of pipelined ops (as opposed to each op)
* `-v, --version`
    * Print version details
* `-R, --rate <T>`
    * work rate (throughput) in requests/sec (total) [Required Parameter]


Numeric arguments may include a SI unit (1k, 1M, 1G)
Time arguments may include a time unit (2s, 2m, 2h)


## Usage

12 Threads, 400 connections, 30 duration

```
wrk -t12 -c400 -d30s http://127.0.0.1:8080/index.html
```

12 Threads, 100 connections, 30 duration, 20000 requests/sec

```
wrk -t2 -c100 -d30s -R2000 http://127.0.0.1:8080/index.html
```

## Reference
- [giltene/wrk2: A constant throughput, correct latency recording variant of wrk](https://github.com/giltene/wrk2)
