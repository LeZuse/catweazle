delimiter ;;


# ----------------------------------------------------------------------------
CREATE TRIGGER bu_products BEFORE UPDATE ON catweazle2011.products FOR EACH ROW 
BEGIN

  # is_new
  IF(NEW.is_new != 0) THEN
    SET NEW.is_new_timestamp = CURRENT_TIMESTAMP;  
  END IF;


END;

 ;;

delimiter ;