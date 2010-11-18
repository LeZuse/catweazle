SET NAMES latin1;
SET FOREIGN_KEY_CHECKS = 0;


DROP TABLE IF EXISTS 
    products, 
    prices, 
    changelog, 
    page_styles, 
    price_styles, 
    price_types, 
    volumes, 
    sections, 
    suppliers, 
    change_categories, 
    product_attribute_types, 
    product_attributes,
    attributes;

DROP TRIGGER IF EXISTS au_log_products;
DROP TRIGGER IF EXISTS ai_log_products;
DROP TRIGGER IF EXISTS au_log_prices;
DROP TRIGGER IF EXISTS ai_log_prices;
DROP TRIGGER IF EXISTS ad_log_prices;
DROP FUNCTION IF EXISTS get_price_type;
DROP FUNCTION IF EXISTS bu_products;
DROP FUNCTION IF EXISTS bu_prices;


SET FOREIGN_KEY_CHECKS = 1;
