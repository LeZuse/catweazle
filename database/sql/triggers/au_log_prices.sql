delimiter ;;


CREATE TRIGGER au_log_prices AFTER UPDATE ON catweazle2011.prices FOR EACH ROW BEGIN
  
  IF(NEW.price_type_id != old.price_type_id) THEN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user)
    
    VALUES
    (NEW.product_id, 
    'prices', 
    CONCAT(get_price_type(OLD.price_type_id), ' ', OLD.minimum_qty, ' @'), 
    CONCAT(get_price_type(NEW.price_type_id), ' ', NEW.minimum_qty, ' @'),
    USER());
  END IF;

  # minimum_qty
  IF(NEW.minimum_qty != old.minimum_qty) THEN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 
    'prices', 
    CONCAT(get_price_type(OLD.price_type_id), ' ', OLD.minimum_qty, ' @'), 
    CONCAT(get_price_type(NEW.price_type_id), ' ', NEW.minimum_qty, ' @'),
    USER());
  END IF;
 
  # price_value
  IF(NEW.price_value != old.price_value) THEN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'Price.price_value', OLD.price_value, NEW.price_value, USER());
  END IF;
  
END;



;;
delimiter ;