import concurrent.futures
import pyspark
import random
import time

from delta import DeltaTable

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from pyspark.sql.functions import broadcast
from pyspark.sql.functions import coalesce, lit
from pyspark.sql.functions import col, cast
from pyspark.sql.functions import col, expr
from pyspark.sql.functions import count
from pyspark.sql.functions import count, lit, desc, col
from pyspark.sql.functions import current_date, current_timestamp
from pyspark.sql.functions import date_format
from pyspark.sql.functions import desc, asc, col
from pyspark.sql.functions import explode
from pyspark.sql.functions import expr
from pyspark.sql.functions import from_json
from pyspark.sql.functions import lit
from pyspark.sql.functions import lit, concat
from pyspark.sql.functions import max, col, desc
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import row_number, desc, col
from pyspark.sql.functions import spark_partition_id
from pyspark.sql.functions import spark_partition_id, count
from pyspark.sql.functions import spark_partition_id, count, lit
from pyspark.sql.functions import sum
from pyspark.sql.functions import to_date
from pyspark.sql.functions import to_json
from pyspark.sql.functions import udf
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import when, col, expr
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.types import _parse_datatype_string
from pyspark.sql.window import Window
