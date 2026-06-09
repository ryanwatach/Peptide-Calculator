def main():
    vial = vial_to_float(input("How many mg per vial? "))
    bac = bac_to_float(input("How many mL of bacteriostatic water are you adding? "))
    dose = dose_to_float(input("How much of the Peptide do you want in each dose? "))
    syringe = syringe_to_float(input("What is the total volume of your syringe? "))
    units = vial / (bac) /100
    print(f"To have a dose of draw {units:.2f} units")


def vial_to_float(v):
    vnew = float(v.replace("$" , "").replace(" dollars", ""))
    return vnew

def bac_to_float(n):
   pnew = float(b.replace("%" , "").replace(" percent", ""))/100
   return pnew

def syringe_to_float(v):
   pnew = float(v.replace("%" , "").replace(" percent", ""))/100
   return pnew
main()
