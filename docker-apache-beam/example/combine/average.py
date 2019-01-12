import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


class AverageFn(beam.CombineFn):

    def create_accumulator(self):
        # (sum_value, count_elem)
        return (0.0, 0)

    def add_input(self, sum_count, input):
        # return an accumator
        (sum, count) = sum_count
        return sum + input, count + 1

    def merge_accumulators(self, accumulators):
        # return merged accumulator
        sums, counts = zip(*accumulators)
        return sum(sums), sum(counts)

    def extract_output(self, sum_count):
        # extract outputs from merged accumator
        (sum, count) = sum_count
        return sum / count if count else float('NaN')


def main():
    data = [1, 10, 100, 1000]
    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        p_d = p | 'create_data' >> beam.Create(data)

        # average
        average = (p_d
                   | 'average' >> beam.CombineGlobally(AverageFn()))
        path_output = os.path.join(PATH_TO_THIS_DIR, 'average.txt')
        (average
         | 'write_average' >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))


if __name__ == '__main__':
    main()
