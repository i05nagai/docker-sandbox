import streaming.processor as processor
import streaming.util as util
import os


def main():
    config = [
        ('spark.driver.memory', '1g'),
        ('spark.executor.memory', '1g'),
    ]
    path_to_this_dir = os.path.abspath(os.path.dirname(__file__))
    path_to_data_dir = os.path.join(path_to_this_dir, '../data')
    path_to_txt = os.path.join(path_to_data_dir, 'data1.json')
    # schema_dict = {
    #     'json_col': {
    #         "str": "StringType",
    #         "num": 'IntegerType',
    #         "str_array": ['StringType'],
    #         "num_array": ['DoubleType'],
    #         "dict": {
    #             "dict_str": 'StringType',
    #             "dict_num": 'DoubleType',
    #             "dict_str_array": ['StringType'],
    #             "dict_num_array": ['DoubleType']
    #         }
    #     }
    # }
    schema_dict = {
        "str": "StringType",
        "num": 'IntegerType',
        "str_array": ['StringType'],
        "num_array": ['DoubleType'],
        "dict": {
            "dict_str": 'StringType',
            "dict_num": 'DoubleType',
            "dict_str_array": ['StringType'],
            "dict_num_array": ['DoubleType']
        }
    }
    schema = util.json_to_schema(schema_dict)
    print(schema)
    # processor.process_socket(config, schema)
    processor.process_file(config, schema)


if __name__ == '__main__':
    main()
