import psycopg2
import os
from dotenv import load_dotenv

# Establish a connection to your PostgreSQL database
load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

connection = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)
cursor = connection.cursor()

# Example SQL INSERT statements for each table
insert_queries = [
    """
   INSERT INTO website_client (id,first_name, last_name, email, phone, nif, address, city, postal_code, create_at)
   VALUES
    (1,'Client1', 'Lastname1', 'client1@example.com', 123456789, 123456789, 'Address1', 'City1', '12345', NOW()),
    (2,'Client2', 'Lastname2', 'client2@example.com', 987654321, 987654321, 'Address2', 'City2', '54321', NOW()),
    (3,'Client3', 'Lastname3', 'client3@example.com', 111222333, 111222333, 'Address3', 'City3', '67890', NOW()),
    (4,'Client4', 'Lastname4', 'client4@example.com', 444555666, 444555666, 'Address4', 'City4', '13579', NOW()),
    (5,'Client5', 'Lastname5', 'client5@example.com', 777888999, 777888999, 'Address5', 'City5', '24680', NOW());
    """,
    """
    INSERT INTO website_supplier (id,first_name, last_name, email, phone, nif, address)
    VALUES
    (1,'Supplier1', 'LastName1', 'supplier1@example.com', 111111111, 123456789, 'Supplier Address 1'),
    (2,'Supplier2', 'LastName2', 'supplier2@example.com', 222222222, 987654321, 'Supplier Address 2'),
    (3, 'Supplier3', 'LastName3', 'supplier3@example.com', 333333333, 444444444, 'Supplier Address 3'),
    (4, 'Supplier4', 'LastName4', 'supplier4@example.com', 444444444, 555555555, 'Supplier Address 4'),
    (5, 'Supplier5', 'LastName5', 'supplier5@example.com', 555555555, 666666666, 'Supplier Address 5');

    """,
    """
    INSERT INTO website_component (id_comp, name, description, price, images, supplier_id)
    VALUES
    (1,'Component1', 'Description for Component 1', 50.00, ARRAY['image1.jpg', 'image2.jpg'], 1),
    (2,'Component2', 'Description for Component 2', 70.00, ARRAY['image3.jpg', 'image4.jpg'], 2),
    (3,'Component3', 'Description for Component 3', 40.00, ARRAY['image5.jpg', 'image6.jpg'], 3),
    (4,'Component4', 'Description for Component 4', 60.00, ARRAY['image7.jpg', 'image8.jpg'], 4),
    (5,'Component5', 'Description for Component 5', 55.00, ARRAY['image9.jpg', 'image10.jpg'], 5);
""",
    """
    INSERT INTO website_labor (id_labor,name, description, price)
    VALUES
        (1,'Labor Type 1', 'Description for Labor Type 1', 100.00),
        (2,'Labor Type 2', 'Description for Labor Type 2', 120.00),
        (3,'Labor Type 3', 'Description for Labor Type 3', 90.00),
        (4,'Labor Type 4', 'Description for Labor Type 4', 110.00),
        (5,'Labor Type 5', 'Description for Labor Type 5', 95.00);
""",
    """
INSERT INTO website_equipment (id_equip,name, description, price, created_at, type_equip, images, quantity, state, type_labor_id)
VALUES
    (1,'Equipment1', 'Description for Equipment 1', 500.00, NOW(), 'Type1', ARRAY['equip_image1.jpg', 'equip_image2.jpg'], 10, 'Active', 1),
    (2,'Equipment2', 'Description for Equipment 2', 700.00, NOW(), 'Type2', ARRAY['equip_image3.jpg', 'equip_image4.jpg'], 15, 'Inactive', 2),
    (3,'Equipment3', 'Description for Equipment 3', 400.00, NOW(), 'Type3', ARRAY['equip_image5.jpg', 'equip_image6.jpg'], 20, 'Active', 3),
    (4,'Equipment4', 'Description for Equipment 4', 600.00, NOW(), 'Type4', ARRAY['equip_image7.jpg', 'equip_image8.jpg'], 12, 'Active', 4),
    (5,'Equipment5', 'Description for Equipment 5', 550.00, NOW(), 'Type5', ARRAY['equip_image9.jpg', 'equip_image10.jpg'], 18, 'Inactive', 5);
""",
    """
    INSERT INTO website_componentusage (component_id, equipment_id)
    VALUES
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3);
""",
    """
INSERT INTO website_stockcomponents (quantity, component_id)
VALUES
    (50, 1),
    (30, 2),
    (40, 3),
    (20, 4),
    (60, 5);
""",
    """
INSERT INTO website_stockequipments (quantity, equipment_id)
VALUES
    (5, 1),
    (8, 2),
    (10, 3),
    (3, 4),
    (7, 5);
""",
    """
INSERT INTO website_purshaseequipment (date, equipment_id, user_id)
VALUES
    ('2023-11-20', 1, 1),
    ('2023-11-21', 2, 2),
    ('2023-11-22', 3, 3),
    ('2023-11-23', 4, 4),
    ('2023-11-24', 5, 5);
""",
    # Add INSERT statements for other tables here
]

try:
    # Execute each INSERT statement
    for query in insert_queries:
        cursor.execute(query)

    # Commit the transaction
    connection.commit()
    print("Data inserted successfully!")

except psycopg2.Error as e:
    connection.rollback()
    print("Error inserting data:", e)

finally:
    # Close cursor and connection
    cursor.close()
    connection.close()
