#!/usr/bin/env sh
mysql -u root -p211573 catweazle2011 < sql/prepare.sql
mysql -u root -p211573 catweazle2011 < sql/tables.sql


mysql -u root -p211573 catweazle2011 < sql/triggers/ai_log_products.sql
mysql -u root -p211573 catweazle2011 < sql/triggers/au_log_products.sql
mysql -u root -p211573 catweazle2011 < sql/triggers/bu_products.sql

mysql -u root -p211573 catweazle2011 < sql/triggers/ai_log_prices.sql
mysql -u root -p211573 catweazle2011 < sql/triggers/au_log_prices.sql
mysql -u root -p211573 catweazle2011 < sql/triggers/ad_log_prices.sql
mysql -u root -p211573 catweazle2011 < sql/triggers/bu_prices.sql


mysql -u root -p211573 catweazle2011 < sql/functions/get_price_type.sql

mysql -u root -p211573 catweazle2011 < sql/views/product_report.sql
mysql -u root -p211573 catweazle2011 < sql/views/price_report.sql

mysql -u root -p211573 catweazle2011 < sql/views/changelog_report.sql

mysql -u root -p211573 catweazle2011 < sql/sample_data/products_HT.sql
mysql -u root -p211573 catweazle2011 < sql/sample_data/prices_HT.sql
