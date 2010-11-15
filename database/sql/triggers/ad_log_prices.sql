delimiter ;;


CREATE TRIGGER ad_log_prices AFTER DELETE ON catweazle2011.prices FOR EACH ROW

BEGIN

 DECLARE change_category INT(11);
 DECLARE field_changed_name VARCHAR(128);

 
 SET change_category = 2; 
 SET field_changed_name = get_price_type(OLD.price_type_id, OLD.minimum_qty);

 INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (OLD.product_id, CONCAT(field_changed_name, ' (removed)'), '', OLD.price_value, USER(), change_category);  

  
END;


;;
delimiter ;