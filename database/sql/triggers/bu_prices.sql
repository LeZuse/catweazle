delimiter ;;


# ----------------------------------------------------------------------------
CREATE TRIGGER bu_prices BEFORE UPDATE ON catweazle2011.prices FOR EACH ROW 
BEGIN


  IF(NEW.is_nlp != 0) THEN
    SET NEW.is_nlp_timestamp = CURRENT_TIMESTAMP;  
  END IF;


END;

 ;;

delimiter ;
