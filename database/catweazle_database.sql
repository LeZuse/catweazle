SET NAMES latin1;
SET FOREIGN_KEY_CHECKS = 0;


/* mysql -u root -p211573 catweazle2011 < 138CW.sql */

DROP TABLE IF EXISTS `products`, `prices`, `changelog`, `page_styles`, `price_styles`, `price_types`, `volumes`, `sections`, `suppliers`;

DROP TRIGGER IF EXISTS `au_log_products`;
DROP TRIGGER IF EXISTS `ai_log_products`;
DROP TRIGGER IF EXISTS `au_log_prices`; /* FUNCTION price_type not implemented yet */
DROP TRIGGER IF EXISTS `ai_log_prices`; /* FUNCTION price_type not implemented yet */
DROP TRIGGER IF EXISTS `ad_log_prices`; /* FUNCTION price_type not implemented yet */

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
CREATE TABLE products (    
    product_id           VARCHAR(16)      NOT NULL        COMMENT 'Hama code',
    product_name         VARCHAR(1024)    DEFAULT ''      COMMENT 'Base product name',
    remark               VARCHAR(1024)    DEFAULT ''      COMMENT 'Base name extension. Pretty much everything after the first comma',
    volume               INT(11)          DEFAULT 1       COMMENT '',
    presenter_section    INT(11)          DEFAULT 24      COMMENT '',
    page_number          INT(11)          DEFAULT NULL    COMMENT '',
    page_style           INT(11)          DEFAULT NULL    COMMENT 'InDesign numbering style',
    is_new               INT(1)           DEFAULT 0       COMMENT 'Presenter NEW status',
    srp                  DECIMAL(10,2)    DEFAULT NULL    COMMENT '',
    qty                  INT(11)          DEFAULT 0       COMMENT '',
    price_style          INT(11)          DEFAULT 1       COMMENT '',
    desc_original        TEXT             DEFAULT ''      COMMENT '',
    desc_presenter       TEXT             DEFAULT ''      COMMENT '',
    supplier_code        VARCHAR(16)      NOT NULL        COMMENT '',
    supplier             INT(11)          DEFAULT 1       COMMENT '',   
    
    PRIMARY KEY  (product_id),
    KEY volume (volume),
    KEY presenter_section (presenter_section),
    KEY price_style (price_style),
    KEY page_style (page_style),
    KEY supplier (supplier),
    
    CONSTRAINT alowed_volumes FOREIGN KEY (volume) REFERENCES volumes (volume_id) ON DELETE NO ACTION ON UPDATE CASCADE,
    CONSTRAINT alowed_sections FOREIGN KEY (presenter_section) REFERENCES sections (section_id) ON DELETE NO ACTION ON UPDATE CASCADE,
    CONSTRAINT alowed_price_styles FOREIGN KEY (price_style) REFERENCES price_styles (price_style_id) ON DELETE NO ACTION ON UPDATE CASCADE,
    CONSTRAINT alowed_page_styles FOREIGN KEY (page_style) REFERENCES page_styles (page_style_id) ON DELETE NO ACTION ON UPDATE CASCADE,
    CONSTRAINT alowed_suppliers FOREIGN KEY (supplier) REFERENCES suppliers (supplier_id) ON DELETE NO ACTION ON UPDATE CASCADE
    
    ) ENGINE=InnoDB
      DEFAULT CHARSET=utf8
      COMMENT='';


# ----------------------------------------------------------------------------
CREATE TABLE prices (
    product_id       VARCHAR(16)      NOT NULL       COMMENT '',
    price_type_id    INT(11)          DEFAULT '1'    COMMENT '',
    minimum_qty      INT(11)          DEFAULT '1'    COMMENT '',
    price_value      DECIMAL(10,2)    NOT NULL       COMMENT '',
    
    PRIMARY KEY  USING BTREE (product_id, price_type_id, minimum_qty),
    KEY price_type_id (price_type_id),
    CONSTRAINT alowed_codes FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE NO ACTION ON UPDATE CASCADE,
    CONSTRAINT price_type_id FOREIGN KEY (price_type_id) REFERENCES price_types (price_type_id) ON DELETE NO ACTION ON UPDATE CASCADE
    ) ENGINE=InnoDB 
      DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------  
CREATE TABLE changelog (        
    change_id           INT(11)         NOT NULL AUTO_INCREMENT                                           COMMENT '',
    product             VARCHAR(16)     NOT NULL                                                          COMMENT '',
    field_changed      VARCHAR(128)    NOT NULL                                                          COMMENT '',
    old_value           TEXT            NOT NULL                                                          COMMENT '',
    new_value           TEXT            NOT NULL                                                          COMMENT '',
    change_timestamp    TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP    COMMENT '',
    made_by_user        VARCHAR(64)     DEFAULT NULL                                                      COMMENT '',    
    
    PRIMARY KEY  (change_id),
    KEY product_code (product),
    CONSTRAINT changelog_alowed_codes FOREIGN KEY (product) REFERENCES products (product_id) ON DELETE NO ACTION ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------
CREATE TABLE page_styles (        
    page_style_id      INT(11)        NOT NULL AUTO_INCREMENT    COMMENT '',
    page_style_name    VARCHAR(32)    DEFAULT NULL               COMMENT '',    
    PRIMARY KEY  (page_style_id),        
    KEY page_style_id (page_style_id)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------
CREATE TABLE price_styles (
    price_style_id      INT(11)        NOT NULL AUTO_INCREMENT  COMMENT '',
    price_style_name    VARCHAR(16)    DEFAULT NULL             COMMENT '',    
    PRIMARY KEY  (`price_style_id`),
    KEY price_style_id (price_style_id)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------
CREATE TABLE price_types (
    price_type_id      INT(11)        NOT NULL      COMMENT '',
    price_type_name    VARCHAR(64)    DEFAULT NULL  COMMENT '',
    PRIMARY KEY  (price_type_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------
CREATE TABLE volumes (
    volume_id      INT(11)        NOT NULL AUTO_INCREMENT    COMMENT '',
    volume_name    VARCHAR(64)    DEFAULT NULL               COMMENT '',
    PRIMARY KEY  (volume_id),
    KEY volume_id (volume_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------
CREATE TABLE suppliers (
    supplier_id      INT(11)        NOT NULL AUTO_INCREMENT    COMMENT '',
    supplier_name    VARCHAR(64)    DEFAULT NULL               COMMENT '',
    PRIMARY KEY  (supplier_id),
    KEY supplier_id (supplier_id)
    ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


# ----------------------------------------------------------------------------
CREATE TABLE sections (
    section_id         INT(11)        NOT NULL        COMMENT '',
    section_code       VARCHAR(4)     DEFAULT NULL    COMMENT '',
    section_name       VARCHAR(64)    DEFAULT NULL    COMMENT '',
    section_ordinal    INT(11)        DEFAULT NULL    COMMENT '',
    PRIMARY KEY  (section_id),
    KEY section_id (section_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

INSERT INTO `suppliers` VALUES
    ('1','not specified'),
    ('2','hama'),
    ('3','Sandisk'),
    ('4','Celestron'),
    ('5','muse');


INSERT INTO `page_styles` VALUES
    ('1','Arabic'),
    ('2','Upper Roman'),
    ('3','Lower Roman'),
    ('4','Upper Letters'),
    ('5','Lower Letters');

INSERT INTO `price_styles` VALUES
    ('1','normal'),
    ('2','New Low Price'),
    ('3','250 Deals');



INSERT INTO `price_types` VALUES
    ('0',''),
    ('1','inv'),
    ('2','mix'),
    ('3','range');

INSERT INTO `sections` VALUES
    ('2','HB','Bags','1'),
    ('3','HC','Cables','2'),
    ('4','HE','Entertainment','3'),
    ('5','HI','Imaging','4'),
    ('6','HM','Multimedia','5'),
    ('7','HP','Power','7'),
    ('8','HT','Tripods','8'),
    ('9','CT','Celestron','9'),
    ('10','KH','Koss','10'),
    ('11','SD','Sandisk','11'),
    ('12','MC','MobileCom','12'),
    ('24','-','Not in the Presenter','0'),
    ('25','SN','Sat Nav','6'),
    ('26','VI','Vivitar','0');



INSERT INTO `volumes` (volume_name) VALUES
    ('Inactive'),
    ('Presenter'),
    ('Sales');


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


delimiter ;;



CREATE TRIGGER ai_log_products AFTER INSERT ON catweazle2011.products FOR EACH ROW 
BEGIN

 INSERT INTO catweazle2011.changelog
  (product, field_changed, old_value, new_value, made_by_user)  
  VALUES
  (NEW.product_id, 'products.product_name', '', NEW.product_name, USER()),
  (NEW.product_id, 'products.remark', '', NEW.remark, USER()),
  (NEW.product_id, 'products.volume', '', NEW.volume, USER()),
  (NEW.product_id, 'products.presenter_section', '', NEW.presenter_section, USER()),
  (NEW.product_id, 'products.page_number', '', NEW.page_number, USER()),
  (NEW.product_id, 'products.page_style', '', NEW.page_style, USER()),
  (NEW.product_id, 'products.desc_presenter', '', NEW.desc_presenter, USER()),
  (NEW.product_id, 'products.desc_original', '', NEW.desc_original, USER()),
  (NEW.product_id, 'products.is_new', '', NEW.is_new, USER()),
  (NEW.product_id, 'products.srp', '', NEW.srp, USER()),
  (NEW.product_id, 'products.qty', '', NEW.qty, USER()),
  (NEW.product_id, 'products.price_style', '', NEW.price_style, USER());

END;

 ;;


# ----------------------------------------------------------------------------
CREATE TRIGGER au_log_products AFTER UPDATE ON catweazle2011.products FOR EACH ROW 
BEGIN

  # product_name
  IF(NEW.product_name != old.product_name) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.product_name', OLD.product_name, NEW.product_name, USER());
  END IF;

  # remark
  IF(NEW.remark != old.remark) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.remark', OLD.remark, NEW.remark, USER());
  END IF;
  
  # volume
  IF(NEW.volume != OLD.volume) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.volume', OLD.volume, NEW.volume, USER());
  END IF;

  # section
  IF(NEW.presenter_section != old.presenter_section) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.presenter_section', OLD.presenter_section, NEW.presenter_section, USER());
  END IF;

  # page_number
  IF(NEW.page_number != old.page_number) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.page_number', OLD.page_number, NEW.page_number, USER());
  END IF;

  # page_style
  IF(NEW.page_style != old.page_style) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.page_style', OLD.page_style, NEW.page_style, USER());
  END IF;

  # desc_presenter
  IF(NEW.desc_presenter != old.desc_presenter) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.desc_presenter', OLD.desc_presenter, NEW.desc_presenter, USER());
  END IF;

  # desc_original
  IF(NEW.desc_original != old.desc_original) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.desc_original', OLD.desc_original, NEW.desc_original, USER());
  END IF;

  # is_new
  IF(NEW.is_new != old.is_new) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.is_new', OLD.is_new, NEW.is_new, USER());
  END IF;

  # srp
  IF(NEW.srp != old.srp) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.srp', OLD.srp, NEW.srp, USER());
  END IF;

  # qty
  IF(NEW.qty != old.qty) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.qty', OLD.qty, NEW.qty, USER());
  END IF;


  # price_style
  IF(NEW.price_style != old.price_style) THEN
    INSERT INTO catweazle2011.changelog 
    (product, field_changed, old_value, new_value, made_by_user)
    VALUES
    (NEW.product_id, 'products.price_style', OLD.price_style, NEW.price_style, USER());
  END IF;


END;

 ;;


/*
Create Trigger `au_log_prices` After Update on `catweazle2011`.`prices` for each row BEGIN
  
  IF(NEW.priceTypeID != old.priceTypeID) THEN
    INSERT INTO `catweazle2011`.`changelog`
    (product_id, columnChanged, oldValue, newValue, user)
    VALUES
    (NEW.product_id, 
    'prices', 
    CONCAT(price_type(OLD.priceTypeID), ' ', OLD.priceAt, ' @'), 
    CONCAT(price_type(NEW.priceTypeID), ' ', NEW.priceAt, ' @'),
    USER());
  END IF;

  # priceAt
  IF(NEW.priceAt != old.priceAt) THEN
    INSERT INTO `catweazle2011`.`changelog`
    (product_id, columnChanged, oldValue, newValue, user)
    VALUES
    (NEW.product_id, 
    'prices', 
    CONCAT(price_type(OLD.priceTypeID), ' ', OLD.priceAt, ' @'), 
    CONCAT(price_type(NEW.priceTypeID), ' ', NEW.priceAt, ' @'),
    USER());
  END IF;
 
  # priceValue
  IF(NEW.priceValue != old.priceValue) THEN
    INSERT INTO `catweazle2011`.`changelog`
    (product_id, columnChanged, oldValue, newValue, user)
    VALUES
    (NEW.product_id, 'Price.priceValue', OLD.priceValue, NEW.priceValue, USER());
  END IF;
  
END;

 ;;
*/


/*
CREATE TRIGGER `ai_log_prices` AFTER UPDATE ON `catweazle2011`.`prices` FOR EACH ROW

BEGIN
    INSERT INTO `catweazle2011`.`changelog`
    (product_id, columnChanged, oldValue, newValue, user)
    
    VALUES
    (NEW.product_id, 
    'prices', 
    '', 
    CONCAT(price_type(NEW.priceTypeID), ' ', NEW.priceAt, ' @'),
    USER()),
    
    (NEW.product_id, 
   CONCAT('prices.', price_type(NEW.priceTypeID), ' ', NEW.priceAt, ' @'), 
    '', 
    NEW.priceValue, USER());

  
END;
*/

/*
CREATE TRIGGER `ad_log_prices` AFTER DELETE ON `catweazle2011`.`prices` FOR EACH ROW

BEGIN
    INSERT INTO `138CW`.`changelog`
    (product_id, columnChanged, oldValue, newValue, user)
    
    VALUES
    (OLD.product_id, 
    'prices', 

    CONCAT(price_type(OLD.priceTypeID), ' ', OLD.priceAt, ' @'),
        '', 
    USER()),
    
    (OLD.product_id, 
   CONCAT('prices.', price_type(OLD.priceTypeID), ' ', OLD.priceAt, ' @'), 
    
    OLD.priceValue, 
    '', 
    USER());

  
END;
*/

 ;;



delimiter ;

/* ------------------------------------------------------------------------------------------ */



SET FOREIGN_KEY_CHECKS = 1;
