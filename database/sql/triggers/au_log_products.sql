delimiter ;;


# ----------------------------------------------------------------------------
CREATE TRIGGER au_log_products AFTER UPDATE ON catweazle2011.products FOR EACH ROW 
BEGIN

 DECLARE change_category INT(11);
 SET change_category = 1;

  # product_name
  IF(NEW.product_name != old.product_name) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.product_name', OLD.product_name, NEW.product_name, USER(), change_category);
  END IF;

  # remark
  IF(NEW.remark != old.remark) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.remark', OLD.remark, NEW.remark, USER(), change_category);
  END IF;
  
  # volume
  IF(NEW.volume != OLD.volume) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.volume', OLD.volume, NEW.volume, USER(), change_category);
  END IF;

  # section
  IF(NEW.presenter_section != old.presenter_section) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.presenter_section', OLD.presenter_section, NEW.presenter_section, USER(), change_category);
  END IF;

  # page_number
  IF(NEW.page_number != old.page_number) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.page_number', OLD.page_number, NEW.page_number, USER(), change_category);
  END IF;

  # page_style
  IF(NEW.page_style != old.page_style) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.page_style', OLD.page_style, NEW.page_style, USER(), change_category);
  END IF;

  # desc_presenter
  IF(NEW.desc_presenter != old.desc_presenter) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.desc_presenter', OLD.desc_presenter, NEW.desc_presenter, USER(), change_category);
  END IF;

  # desc_original
  IF(NEW.desc_original != old.desc_original) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.desc_original', OLD.desc_original, NEW.desc_original, USER(), change_category);
  END IF;

  # is_new
  IF(NEW.is_new != old.is_new) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.is_new', OLD.is_new, NEW.is_new, USER(), change_category);
  END IF;
  
  # srp
  IF(NEW.srp != old.srp) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.srp', OLD.srp, NEW.srp, USER(), change_category);
  END IF;

  # qty
  IF(NEW.qty != old.qty) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.qty', OLD.qty, NEW.qty, USER(), change_category);
  END IF;


  # price_style
  IF(NEW.price_style != old.price_style) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user, change_category)
    VALUES
    (NEW.product_id, 'products.price_style', OLD.price_style, NEW.price_style, USER(), change_category);
  END IF;


END;

 ;;

delimiter ;