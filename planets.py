planet_list = ["Mercury", "Mars"]

print("Planet List:", planet_list)
print("\n\n")

planet_list.append("Jupiter")
planet_list.append("Saturn")
print("Planet List After Add:", planet_list)
print("\n\n")

localPlanets = ["Uranus", "Neptune"]
planet_list.extend(localPlanets)
print("Local planets:", localPlanets)
print("Planet List After Extend:", planet_list)
print("\n\n")

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print("Planet List After Insert:", planet_list)
print("\n\n")

planet_list.append("Pluto")
print("Planet List After Append:", planet_list)
print("\n\n")

rocky_planets = planet_list[0:4]
print("Rocky planets", rocky_planets)
print("Planet List After `Slice`:", planet_list)
print("\n\n")

planet_list.remove("Pluto")
print("Planet List After `Del`:", planet_list)
print("\n\n")
