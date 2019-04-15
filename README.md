# Mountain Project Route Scraping

## Scrapes info for personal use

area2routeNameLink.py
- takes data2.csv with list of areas and yields a file with area_name, route_name, and route_link

routeLink2RouteInfo.py
- takes data3.csv with list of route_link and yields a file with area_name, route_name, yds_rating, user_rating, climb_type_and_height, first_ascent, description, and protection




## To do:
- Fix high tiered area names (Still "Giggling to the Graveyard" is too long?)
- Fix star ratings
- Fix description/Location/Getting There pulls. Maybe add search feature?
- Get route page links properly. Go through areas and if a link in areas is another area then add it to another file until they are all route pages?
- pull photos?
- pull comments? tough because they're unique numbers