from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def write_to_file(pipeline, id_str):
    PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))
    path_output = os.path.join(PATH_TO_THIS_DIR, '{0}.txt'.format(id_str))
    (pipeline
     | 'write_{0}'.format(id_str) >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))


def main():
    data = [
        ('a', 1, 100,),
        ('b', 2, 100,),
        ('c', 1, 100,),
        ('d', 2, 100,),
        ('e', 1, 100,),
        ('f', 1, 100,),
        ('g', 1, 100,),
        ('h', 1, 100,),
        ('i', 1, 100,),
    ]

    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        students = p | 'create_data' >> beam.Create(data)

        class CreateKeyValue(beam.DoFn):

            def process(self, element):
                return [(element[0], (element[1], element[2]))]

        fixed_window = (
            students
            | 'fixed_window' >> beam.WindowInto(beam.window.FixedWindows(60))
            | 'fixed_window_do_fn' >> beam.ParDo(CreateKeyValue())
            | 'fixed_window_group' >> beam.GroupByKey())
        write_to_file(fixed_window, 'fixed_window')

        sliding_window = (
            students
            | 'sliding_window' >> beam.WindowInto(beam.window.SlidingWindows(30, 5))
            | 'sliding_window_do_fn' >> beam.ParDo(CreateKeyValue())
            | 'sliding_window_group' >> beam.GroupByKey())
        write_to_file(sliding_window, 'sliding_window')

        session_window = (
            students
            | 'session_window' >> beam.WindowInto(beam.window.Sessions(10 * 60))
            | 'session_window_do_fn' >> beam.ParDo(CreateKeyValue())
            | 'session_window_group' >> beam.GroupByKey())
        write_to_file(session_window, 'session_window')

        global_window = (
            students
            | 'global_window' >> beam.WindowInto(beam.window.GlobalWindows())
            | 'global_window_do_fn' >> beam.ParDo(CreateKeyValue())
            | 'global_window_group' >> beam.GroupByKey())
        write_to_file(global_window, 'global_window')


if __name__ == '__main__':
    main()
