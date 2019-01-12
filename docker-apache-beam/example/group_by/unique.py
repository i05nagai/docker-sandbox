from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


class CreateKeyValue(beam.DoFn):

    def process(self, element):
        return [(element, element)]


class ExtractKey(beam.DoFn):

    def process(self, element):
        return [element[0][0]]


def main():
    #
    # An example of simple join (i.e. GroupByKey)
    #
    p = beam.Pipeline(options=pipeline_options.PipelineOptions())
    #
    # email
    #
    name_list = [
        ('amy',),
        ('carl',),
        ('julia',),
        ('carl',),
        ('julia',),
        ('carl',),
        ('julia',),
        ('carl',),
    ]
    path_output = os.path.join(PATH_TO_THIS_DIR, 'name.txt')
    name = p | 'create_name' >> beam.Create(name_list)
    name | 'write_name' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # group by
    #
    group_by = (name
                | beam.ParDo(CreateKeyValue())
                | beam.GroupByKey()
                | beam.ParDo(ExtractKey()))
    path_output = os.path.join(PATH_TO_THIS_DIR, 'unique.txt')
    group_by | 'write_unique' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # wait
    #
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    main()
