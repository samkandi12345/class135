import csv
import plotly_express as pe
rows = []

with open("data.csv") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
#print(headers)
#print(planet_data_rows)

headers[0] = "row_num"
solar_system_planet_count = {}
for planet_data in planet_data_rows:
    if solar_system_planet_count.get(planet_data[11]):
        solar_system_planet_count[planet_data[11]]+=1
    else:
        solar_system_planet_count[planet_data[11]]=1
    
max_solar_system = max(solar_system_planet_count,key = solar_system_planet_count.get)
print("solar system {} has maximum planets {} out of all the solar system we have discovered so far".format(max_solar_system,solar_system_planet_count[max_solar_system]))

KOI_351_planets = []
for planet_data in planet_data_rows:
    if max_solar_system == planet_data[11]:
        KOI_351_planets.append(planet_data)
    
print(len(KOI_351_planets))
print(KOI_351_planets)

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[3]
    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiter":
            planet_mass_value = float(planet_mass_value)*317.8
        
        planet_data[3] = planet_mass_value

    
    planet_radius = planet_data[7]
    if planet_radius.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
        if planet_radius_ref == "Jupiter":
            planet_radius_value = float(planet_radius_value)*11.2

        planet_data[7] = planet_radius_value

print(len(planet_data_rows))
KOI_351_planets = []

KOI_351_planets_masses = []
KOI_351_planets_names = []
for planet_data in KOI_351_planets:
    KOI_351_planets_masses.append(planet_data[3])
    KOI_351_planets_names.append(planet_data[1])

KOI_351_planets_masses.append(1)
KOI_351_planets_names.append("Earth")
#figure = pe.bar(x=KOI_351_planets_names,y=KOI_351_planets_masses)
#figure.show()

temp_planet_data_rows = list(planet_data_rows)
for planet_data in planet_data_rows:
    if planet_data[1].lower() == "Kepler-903 b":
        planet_data_rows.remove(planet_data)
        
planet_masses = []
planet_radii = []
planet_names = []

for planet_data in planet_data_rows:
    planet_masses.append(planet_data[3])
    planet_radii.append(planet_data[7])
    planet_names.append(planet_data[1])

planet_gravity = []

for index,name in enumerate(planet_names):
    gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radii[index])*float(planet_radii[index])*6371000*6371000) * 6.674e-11
    planet_gravity.append(gravity)

figure = pe.scatter(x=planet_radii,y=planet_mass,size = planet_gravity,hover_data=[planet_mass])
figure.show()

low_grv_pla = []

#for index,gravity in enumerate(planet_gravity):
 #   if gravity<10:
  #      low_grv_pla.append(planet_data_rows[index])
#print(len(low_grv_pla))

#low_grv_pla = []
#for index,gravity in enumerate(planet_gravity):
 #   if gravity<100:
  #      low_grv_pla.append(planet_data_rows[index])
#print(len(low_grv_pla))


print(headers)

planet_type_value = []
for planet_data in planet_data_rows:
    planet_type_value.append(planet_data[6])

print(list(set(planet_type_value)))

planet_mass = []
planet_radius = []


    

    



