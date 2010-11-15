DROP VIEW IF EXISTS changelog_report;

CREATE ALGORITHM=UNDEFINED DEFINER=root@localhost SQL SECURITY DEFINER VIEW changelog_report AS 

SELECT 
	date_format(`changelog`.`change_timestamp`,_utf8'%d/%m/%Y %H:%i:%s') AS "date", 
	changelog.product, 
	
	IF(products.remark = '', products.product_name, CONCAT(products.product_name, ', ', products.remark)) AS 'Name',
	

	
	
	
	changelog.field_changed, 
	changelog.old_value, 
	changelog.new_value, 
	volumes.volume_name,
	sections.section_code, 
	products.page_number, 	
	
	
	changelog.made_by_user, 
	change_categories.change_category_name
	 
	

	
FROM change_categories INNER JOIN changelog ON change_categories.change_category_id = changelog.change_category
	 INNER JOIN products ON products.product_id = changelog.product
	 INNER JOIN sections ON sections.section_id = products.presenter_section
	 INNER JOIN volumes ON volumes.volume_id = products.volume

ORDER BY change_timestamp DESC

WITH CASCADED CHECK OPTION;
