product_name = "Клавіатура"
price = 450
is_sale = False
is_available = True

if not is_available:
    print(f"Товар {product_name} тимчасово відсутній на складі.")
else:
    if price <= 500 or is_sale:
        category = "Budget / Promotional"
    elif 501 <= price <= 1000:
        category = "Standard"
    else:
        category = "Premium"

    print(f"Товар: {product_name} | Ціна: {price} | Категорія: {category}")