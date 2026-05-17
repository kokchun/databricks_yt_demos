from pyspark import pipelines as dp 
from pyspark.sql.functions import coalesce, lit, when, col, to_timestamp
from utils.utils import rename_columns_to_snake_case

@dp.table(name="supply_chain_demo.silver.supply_chain_obt",
          comment="Cleaned supply chain data for DataCo",
        table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5"
    })
def cleaned_supply_chain():
    df = rename_columns_to_snake_case(spark.sql("SELECT * FROM STREAM supply_chain_demo.bronze.raw_supply_chain"))

    return (
        df.withColumn("customer_lname", coalesce("customer_lname", lit("-"))).withColumn(
            "shipping_date",
            to_timestamp(col("shipping_date_(dateorders)"), "M/d/yyyy H:mm"),
        )
        .withColumn(
            "customer_zipcode",
            coalesce(col("customer_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "order_zipcode", coalesce(col("order_zipcode").cast("string"), lit("unknown"))
        )
        .withColumn(
            "customer_country",
            when(col("customer_country") == "EE. UU.", "United States").otherwise(
                col("customer_country")
            ),
        )
    ).drop("product_description", "customer_email", "customer_password", "shipping_date_(dateorders)")


