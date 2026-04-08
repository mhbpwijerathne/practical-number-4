
weight = float(input("Enter weight"))

if weight <= 20 :
    print ("no charge")

elif weight <= 30 :
    extra_kg = weight -20
    charge = extra_kg * 200
    print("Extra weight: " + str(extra_kg) + " kg")
    print("Extra charge: Rs. " + str(charge))

else:
    print("Baggage exceeds 30kg. This baggage is not allowed.")

