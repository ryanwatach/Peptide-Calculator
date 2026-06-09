def main():
    vial = vial_to_float(input("How many mg per vial? ")).lower()
    bac = bac_to_float(input("How many mL of bacteriostatic water are you adding? ")).lower()
    dose = dose_to_float(input("How many mg of the peptide do you want in each dose? ")).lower()
    units_per_ml = vial / (bac)
    correct_dose = dose/(units_per_ml) * 100
    print(f"To have a dose of {dose:.2f} in a 1 mL syringe, draw {units_per_ml:.2f}")


def vial_to_float(v):
    vnew = float(v.replace("mg" , "").replace(" dollars", ""))
    return vnew

def bac_to_float(b):
   pnew = float(b.replace("ml" , "").replace("millileters", ""))
   return pnew

def dose_to_float(d):
   pnew = float(d.replace("%" , "").replace(" percent", ""))
   return pnew

main()
