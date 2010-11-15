DROP VIEW IF EXISTS price_report;

CREATE ALGORITHM=UNDEFINED DEFINER=root@localhost SQL SECURITY DEFINER VIEW price_report AS 

SELECT 
	prices.product_id AS `'Code'`, 
	products.product_name AS `'Name'`, 
	products.srp, 	

CONCAT(GROUP_CONCAT(CONCAT(prices.minimum_qty, ':', prices.price_value) )) AS INV,



sections.section_code AS `'Section'`, 

	
	products.page_number AS 'Page'
FROM 
prices 

INNER JOIN products ON prices.product_id = products.product_id
INNER JOIN sections ON sections.section_id = products.presenter_section



GROUP BY prices.product_id


ORDER BY products.page_number, prices.product_id ASC


