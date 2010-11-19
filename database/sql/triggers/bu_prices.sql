delimiter ;;


# ----------------------------------------------------------------------------
CREATE TRIGGER bu_prices BEFORE UPDATE ON catweazle2011.prices FOR EACH ROW 
BEGIN

  IF(NEW.price_value < OLD.price_value) THEN 
    SET NEW.is_nlp = 1;
    SET NEW.is_nlp_timestamp = CURRENT_TIMESTAMP; 
  END IF;




END;

 ;;

delimiter ;
