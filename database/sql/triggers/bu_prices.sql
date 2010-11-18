delimiter ;;


# ----------------------------------------------------------------------------
CREATE TRIGGER bu_prices BEFORE UPDATE ON catweazle2011.prices FOR EACH ROW 
BEGIN

  IF(NEW.price_value < OLD.price_value) THEN 
    SET NEW.is_nlp = 1;
  END IF;

  IF(NEW.is_nlp != 0) THEN
    SET NEW.is_nlp_timestamp = CURRENT_TIMESTAMP;  
  END IF;


END;

 ;;

delimiter ;
