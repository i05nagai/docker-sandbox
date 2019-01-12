from apache_beam.testing.util import assert_that
from apache_beam.testing.util import equal_to
from apache_beam.testing.test_pipeline import TestPipeline
import apache_beam as beam
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


with TestPipeline() as p:
    assert_that(p | beam.Create([1, 2, 3]), equal_to([1, 2, 3]))
    path_output = os.path.join(PATH_TO_THIS_DIR, 'foobar.txt')
    p_o = p | 'Write' >> beam.Create([1, 2, 3])
    p_o | beam.io.WriteToText(path_output, file_name_suffix='.csv')
