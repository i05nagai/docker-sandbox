import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def main():
    data1 = [
        ('a', 1, 100,),
        ('b', 2, 100,),
    ]
    data2 = [
        ('c', 1, 100,),
        ('d', 2, 100,),
    ]
    data3 = [
        ('e', 1, 100,),
    ]
    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        p1 = p | 'create_data1' >> beam.Create(data1)
        p2 = p | 'create_data2' >> beam.Create(data2)
        p3 = p | 'create_data3' >> beam.Create(data3)

        # flatten
        flatten = ((p1, p2, p3)
                   | 'flatten' >> beam.Flatten())
        path_output = os.path.join(PATH_TO_THIS_DIR, 'flatten.txt')
        (flatten
         | 'write_flatten' >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))


if __name__ == '__main__':
    main()
