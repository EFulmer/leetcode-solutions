select product_name, sales.year, sales.price
from sales
inner join product on product.product_id = sales.product_id;
