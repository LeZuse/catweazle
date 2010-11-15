delimiter ;;




CREATE FUNCTION get_price_type(
    price_type_id   INT(11),
    minimum_qty     INT(11))
    
    RETURNS VARCHAR(128)
    DETERMINISTIC
    
    BEGIN
    
        DECLARE price_type VARCHAR(64);
        DECLARE output VARCHAR(128);
        
        SET price_type = '';

        IF(price_type_id = 1) THEN
          SET price_type = 'INV';
        END IF;

        IF(price_type_id = 2) THEN
          SET price_type = 'MIX';
        END IF;
        
        IF(price_type_id = 3) THEN
          SET price_type = 'RANGE';
        END IF;        


        
        SET output = CONCAT(price_type, ' @ ', minimum_qty);
        
        
        RETURN(output);
    
    END
    
;;

delimiter ;

