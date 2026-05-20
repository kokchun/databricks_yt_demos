from pyspark import pipelines as dp
from pyspark.sql.functions import (
    coalesce,
    lit,
    when,
    col,
    to_timestamp,
    round as spark_round,
    initcap,
)
from utils.utils import rename_columns_to_snake_case


@dp.table(
    name="supply_chain_demo.silver.supply_chain_obt",
    comment="Cleaned supply chain data for DataCo",
    table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5",
    },
)
def cleaned_supply_chain():
    df = rename_columns_to_snake_case(
        spark.sql("SELECT * FROM STREAM supply_chain_demo.bronze.raw_supply_chain")
    )

    return (
        df.withColumn("customer_lname", coalesce("customer_lname", lit("-")))
        .withColumn(
            "shipping_date",
            to_timestamp(col("shipping_date_(dateorders)"), "M/d/yyyy H:mm"),
        )
        .withColumn(
            "customer_zipcode",
            coalesce(col("customer_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "order_zipcode",
            coalesce(col("order_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "customer_country",
            when(col("customer_country") == "EE. UU.", "United States").otherwise(
                col("customer_country")
            ),
        )
        .withColumn(
            "order_date", to_timestamp(col("order_date_(dateorders)"), "M/d/yyyy H:mm")
        )
        .withColumn("product_name", initcap("product_name"))
        .withColumn(
            "customer_state",
            when(
                (col("customer_state") == "91732") | (col("customer_state") == "95758"),
                "CA",
            ).otherwise(col("customer_state")),
        )
        .withColumn("product_price", spark_round(col("product_price"), 2))
        .withColumn(
            "order_item_discount_rate", spark_round(col("order_item_discount_rate"), 2)
        )
        .withColumn(
            "order_item_product_price", spark_round(col("order_item_product_price"), 2)
        )
    ).drop(
        "product_description",
        "customer_email",
        "customer_password",
        "shipping_date_(dateorders)",
    )