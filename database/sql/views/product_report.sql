DROP VIEW IF EXISTS product_report;

CREATE ALGORITHM=UNDEFINED 
DEFINER=root@localhost 
SQL SECURITY DEFINER VIEW product_report 

AS 

SELECT      products.product_id,
            products.product_name,
            products.remark,
            volumes.volume_name,
            sections.section_code,
            products.page_number,
            products.is_new,
            products.is_new_timestamp,
#             products.is_nlp,
#             products.is_nlp_timestamp,
            products.qty,
            price_styles.price_style_name,
            products.supplier_code,
            suppliers.supplier_name,
            products.srp,
            
            GROUP_CONCAT(
                CONCAT(
                    price_types.price_type_name, 
                    ':', 
                    prices.minimum_qty, 
                    ':', 
                    prices.price_value
                    )
                ) AS 'invoice'

FROM        products 
            JOIN volumes ON volumes.volume_id = products.volume
            JOIN sections ON sections.section_id = products.presenter_section
            JOIN page_styles ON page_styles.page_style_id = products.page_style
            JOIN price_styles ON price_styles.price_style_id = products.price_style
            JOIN suppliers ON suppliers.supplier_id = products.supplier_id    
            LEFT JOIN prices ON prices.product_id = products.product_id
            LEFT JOIN price_types ON price_types.price_type_id = prices.price_type_id

GROUP BY    products.product_id

ORDER BY    sections.section_ordinal, 
            products.page_number, 
            prices.product_id ASC

# WITH CASCADED CHECK OPTION;
