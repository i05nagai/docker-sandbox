
## Note
* Apache Beam SDKs does not support python3

### nose
If you use TestPipeline, nose is required

```
Traceback (most recent call last):
  File "/usr/lib/python2.7/runpy.py", line 174, in _run_module_as_main
    "__main__", fname, loader, pkg_name)
  File "/usr/lib/python2.7/runpy.py", line 72, in _run_code
    exec code in run_globals
  File "/tmp/repository/src/beam_sample.py", line 3, in <module>
    from apache_beam.testing.test_pipeline import TestPipeline
  File "/root/.local/lib/python2.7/site-packages/apache_beam/testing/test_pipeline.py", line 25, in <module>
    from nose.plugins.skip import SkipTest
ImportError: No module named nose.plugins.skip
```


## Reference
* [Beam Docker Images](https://beam.apache.org/contribute/docker-images/)
* https://github.com/apache/beam/tree/master/sdks/java/build-tools/src/main/resources/docker
