def main():
    # ask for mg/vial, bac water amount, and the dosage required
    vial = vial_to_float(input("How many mg per vial? ").lower())
    bac = bac_to_float(input("How many mL of bacteriostatic water are you adding? ").lower())
    dose = dose_to_float(input("How many mg of the peptide do you want in each dose? ").lower())
    
    # mg of peptide per 1 mL of fluid
    mg_per_ml = vial / (bac)

    # standard U-100 insulin syringe conversion (100 units = 1 mL)
    # (dose / concentration) * 100 units
    correct_dose = dose/(mg_per_ml) * 100
    print(f"To have a dose of {dose:.2f} in a 1 mL syringe, draw {correct_dose:.2f} units")

# removes unwanted text
def vial_to_float(v):
    vnew = float(v.replace("mg" , "").replace(" miligrams", ""))
    return vnew

def bac_to_float(b):
   pnew = float(b.replace("ml" , "").replace("millileters", ""))
   return pnew

def dose_to_float(d):
   pnew = float(d.replace("mg" , "").replace(" miligrams", ""))
   return pnew

main()
