import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def bounded_sum(values, bound=500):
    return min(sum(values), bound)


def main():
    data = [1, 10, 100, 1000]
    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        p_d = p | 'create_data' >> beam.Create(data)

        # small
        # [500]
        small_sum = (p_d
                     | 'small_sum' >> beam.CombineGlobally(bounded_sum))
        path_output = os.path.join(PATH_TO_THIS_DIR, 'small_sum.txt')
        (small_sum
         | 'write_small_sum' >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))

        # large
        # [1111]
        large_sum = (p_d
                     | 'large_sum' >> beam.CombineGlobally(bounded_sum, bound=5000))
        path_output = os.path.join(PATH_TO_THIS_DIR, 'large_sum.txt')
        (large_sum
         | 'write_large_sum' >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))


if __name__ == '__main__':
    main()
