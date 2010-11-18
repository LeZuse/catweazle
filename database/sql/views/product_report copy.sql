DROP VIEW IF EXISTS product_report;

CREATE ALGORITHM=UNDEFINED DEFINER=root@localhost SQL SECURITY DEFINER VIEW product_report AS 

SELECT 
products.product_id AS 'Code',
products.product_name AS 'Name',
products.remark AS 'Detail',
volumes.volume_name AS 'Volume',
sections.section_code AS 'Section',
products.page_number AS 'Page',
products.is_new AS 'New',
products.srp AS 'SRP',
products.qty AS 'Quantity',
price_styles.price_style_name AS price_style_name,
products.supplier_code AS 'Supplier Code',
suppliers.supplier_name AS 'Supplier' 

FROM 
volumes 
JOIN products ON volumes.volume_id = products.volume
JOIN sections ON sections.section_id = products.presenter_section
JOIN page_styles ON page_styles.page_style_id = products.page_style
JOIN price_styles ON price_styles.price_style_id = products.price_style
JOIN suppliers ON suppliers.supplier_id = products.supplier



WITH CASCADED CHECK OPTION;
