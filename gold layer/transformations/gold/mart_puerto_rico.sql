USE CATALOG supply_chain_demo;
USE SCHEMA gold;

CREATE OR REFRESH MATERIALIZED VIEW supply_chain_demo.gold.mart_puerto_rico
  COMMENT "Serving view - gold layer" AS
SELECT 
    o.order_id,
    o.order_status,
    ol.total_amount,
    p.product_name,
    p.category_name,
    d.datetime,
    d.year,
    d.weekday,
    c.country,
    c.state,
    c.segment
FROM  fct_orderlines ol 
LEFT JOIN dim_customer c ON ol.customer_id = c.customer_id
LEFT JOIN dim_date d ON ol.order_date_id = d.datetime_id
LEFT JOIN dim_order o ON ol.order_id = o.order_id
LEFT JOIN dim_product p ON ol.product_id = p.product_id
WHERE c.country = 'Puerto Rico'