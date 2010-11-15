SET NAMES latin1;
SET FOREIGN_KEY_CHECKS = 0;



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
    field_changed       VARCHAR(128)    NOT NULL                                                          COMMENT '',
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

INSERT INTO suppliers VALUES
    ('1','not specified'),
    ('2','hama'),
    ('3','Sandisk'),
    ('4','Celestron'),
    ('5','muse');


INSERT INTO page_styles VALUES
    ('1','Arabic'),
    ('2','Upper Roman'),
    ('3','Lower Roman'),
    ('4','Upper Letters'),
    ('5','Lower Letters');

INSERT INTO price_styles VALUES
    ('1','normal'),
    ('2','New Low Price'),
    ('3','250 Deals');



INSERT INTO price_types VALUES
    ('0',''),
    ('1','inv'),
    ('2','mix'),
    ('3','range');

INSERT INTO sections VALUES
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



INSERT INTO volumes (volume_name) VALUES
    ('Inactive'),
    ('Presenter'),
    ('Sales');



SET FOREIGN_KEY_CHECKS = 1;
