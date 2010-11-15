delimiter ;;


CREATE TRIGGER ad_log_prices AFTER DELETE ON catweazle2011.prices FOR EACH ROW

BEGIN
    INSERT INTO catweazle2011.changelog
    (product, field_changed, old_value, new_value, made_by_user)
    
    VALUES
    (OLD.product_id, 
    'prices', 

    CONCAT(get_price_type(OLD.price_type_id), ' ', OLD.minimum_qty, ' @'),
        '', 
    USER()),
    
    (OLD.product_id, 
   CONCAT('prices.', get_price_type(OLD.price_type_id), ' ', OLD.minimum_qty, ' @'), 
    
    OLD.price_value, 
    '', 
    USER());

  
END;


;;
delimiter ;