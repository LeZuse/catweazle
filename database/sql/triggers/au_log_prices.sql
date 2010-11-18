delimiter ;;


CREATE TRIGGER au_log_prices AFTER UPDATE ON catweazle2011.prices FOR EACH ROW BEGIN


 DECLARE change_category INT(11);
 DECLARE field_changed_name VARCHAR(128);

 
 SET change_category = 2; 
 SET field_changed_name = get_price_type(OLD.price_type_id, OLD.minimum_qty);  

  IF(NEW.price_type_id != OLD.price_type_id) THEN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user, change_category)    
    VALUES
    (NEW.product_id, CONCAT(field_changed_name, ' (price_type_id)'), OLD.price_type_id, NEW.price_type_id, USER(), change_category);
  END IF;

  # minimum_qty
  IF(NEW.minimum_qty != OLD.minimum_qty) THEN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user, change_category)    
    VALUES
    (NEW.product_id, CONCAT(field_changed_name, ' (minimum_qty)'), OLD.minimum_qty, NEW.minimum_qty, USER(), change_category);
  END IF;


 
  # price_value
  IF(NEW.price_value != old.price_value) THEN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, CONCAT(field_changed_name, ' (price_value)'), OLD.price_value, NEW.price_value, USER(), change_category);
  

    
  END IF;
 
END;



;;
delimiter ;
