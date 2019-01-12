from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


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
        students = p | 'create_data1' >> beam.Create(data)

        def partition_fn(student, num_partitions):
            print(student)
            return ord(student[0]) % num_partitions

        by_decile = students | 'by_decile' >> beam.Partition(partition_fn, 5)
        path_output = os.path.join(PATH_TO_THIS_DIR, 'by_decile.txt')
        (by_decile
         | 'write_flatten' >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))


if __name__ == '__main__':
    main()
