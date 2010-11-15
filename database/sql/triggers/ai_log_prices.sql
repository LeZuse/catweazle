delimiter ;;



CREATE TRIGGER ai_log_prices AFTER INSERT ON catweazle2011.prices FOR EACH ROW

BEGIN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user)
    
    VALUES
    (NEW.product_id, 
    'prices', 
    '', 
    CONCAT(get_price_type(NEW.price_type_id), ' ', NEW.minimum_qty, ' @'),
    USER()),
    
    (NEW.product_id, 
   CONCAT('prices.', get_price_type(NEW.price_type_id), ' ', NEW.minimum_qty, ' @'), 
    '', 
    NEW.price_value, USER());

  
END;


;;
delimiter ;