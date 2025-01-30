import sqlite3
import math


def create_database():
    """Create SQLite database and table if not exists."""
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                        name TEXT PRIMARY KEY,
                        latitude REAL,
                        longitude REAL)''')
    conn.commit()
    conn.close()


def get_city_coordinates(city):
    """Retrieve city coordinates from database or ask user to input them."""
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude FROM cities WHERE name = ?", (city,))
    result = cursor.fetchone()

    if result:
        conn.close()
        return result

    lat = float(input(f"Enter latitude for {city}: "))
    lon = float(input(f"Enter longitude for {city}: "))

    cursor.execute("INSERT INTO cities (name, latitude, longitude) VALUES (?, ?, ?)", (city, lat, lon))
    conn.commit()
    conn.close()

    return lat, lon


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on Earth using the Haversine formula."""
    R = 6371  # Radius of Earth in kilometers
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def main():
    create_database()

    #    city1 = input("Enter the first city: ")
    #    city2 = input("Enter the second city: ")
    city1 = "Tokyo, Japan"
    city1_lat = 35.6762
    city1_lon = 139.6503

    city2 = "Rio de Janeiro, Brazil"

    city2_lat = -22.9068
    city2_lon = -43.1729
    # lat1, lon1 = get_city_coordinates(city1)
    # lat2, lon2 = get_city_coordinates(city2)

    distance = haversine_distance(city1_lat, city1_lon, city2_lat, city2_lon)
    print(f"The distance between {city1} and {city2} is {distance:.2f} km")


if __name__ == "__main__":
    main()
