import pyspark
import json
import pyspark.sql
import pyspark.sql.functions as f
from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


def get_data(spark):
    data = """
[
  {
    "friends": [
      {
        "id": 0,
        "name": "Georgina Sears"
      },
      {
        "id": 1,
        "name": "Miranda Tillman"
      },
      {
        "id": 2,
        "name": "Rosario Doyle"
      }
    ]
  },
  {
    "friends": [
      {
        "id": 0,
        "name": "Manuela Noble"
      },
      {
        "id": 1,
        "name": "Aguilar Roy"
      },
      {
        "id": 2,
        "name": "Holt Espinoza"
      }
    ]
  },
  {
    "friends": [
      {
        "name": "Manuela Noble"
      },
      {
        "name": "Aguilar Roy"
      },
      {
        "id": 2,
        "name": "Holt Espinoza"
      }
    ]
  }
]
    """
    data_dict = json.loads(data)
    schema = StructType().add(
        "friends", ArrayType(
            StructType([
                StructField("id", StringType()),
                StructField("name", StringType())
            ])
        )
    )
    df = spark.createDataFrame(data_dict, schema)
    print(df.show(truncate=False))
    print(df.toJSON().collect())
    return df


def main():
    spark = pyspark.sql.SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
    df = get_data(spark)
    extract_field3(df)


def extract_field(spark, df):
    text = 'bbbb'
    df = spark.createDataFrame([('A$B', 'a$b$c')], ['k', 's'])
    df.select(
        f.sha1(f.split(f.col('s'), '\$')).alias('k')
    ).withColumn(
        'k', f.when(
            f.col('k') == f"{text}$",
            f.concat(
                f.lit(f"{text}-"),
                f.sha1(F.split(F.col("s"), "\$").getItem(0))
            )
        ).otherwise(F.col('k'))
    ).collect()


def extract_field2(df):
    data = df.select(
        f.col('friends.id')
    ).collect()
    print(data)


def extract_field3(df):
    data = df.select(
        f.coalesce(f.col('friends.id')).alias('ids')
    )
    data.show()


if __name__ == '__main__':
    main()
