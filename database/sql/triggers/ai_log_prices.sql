delimiter ;;



CREATE TRIGGER ai_log_prices AFTER INSERT ON catweazle2011.prices FOR EACH ROW

BEGIN

 DECLARE change_category INT(11);
 DECLARE field_changed_name VARCHAR(128);

 
 SET change_category = 2; 
 SET field_changed_name = get_price_type(NEW.price_type_id, NEW.minimum_qty);
 
 INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, CONCAT(field_changed_name, ' (created)'), '', NEW.price_value, USER(), change_category);  
END;


;;
delimiter ;