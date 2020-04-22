# Here I show how can we use PostgreSQL extension called PostGIS.

# It's example which print shapes that are within 1 km of a point of interest:


import psycopg2


def main():
    conn = psycopg2.connect(database='postgis', user='postgres')
    curs = conn.cursor()

    # Find the distance within 1 km of point-of-interest
    poi = (-124.3, 53.2)  # longitude, latitude

    # Table 'my_points' has a geography column 'geog'
    curs.execute("""\
    SELECT gid, ST_AsGeoJSON(geog), ST_Distance(geog, poi)
    FROM my_points, (SELECT ST_MakePoint(%s, %s)::geography AS poi) AS f
    WHERE ST_DWithin(geog, poi, 1000);""", poi)

    for row in curs.fetchall():
        print(row)


if __name__ == '__main__':
    main()
