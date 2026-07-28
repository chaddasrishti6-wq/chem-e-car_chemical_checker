
import pandas as pd

limits = {"acetic acid": 0.5, "hydrochloric acid": 0.1, "sulfuric acid": 0.3}
banned = ["nitric acid"]
allowed_peroxide_conc = 0.3


def check_acid(chemical, concentration):
    if chemical.lower() in banned:
        print(f"{chemical} is a banned chemical. You may not proceed with its use")
    else:
        if chemical.lower() in limits:
            if concentration > limits[chemical.lower()]:
                print(f"a concentration of {concentration} exceeds the allowed concentration for {chemical}, which is {limits[chemical.lower()]}")
            else:
                print(f"a concentration of {concentration} is within the allowed concentration for {chemical}. You may proceed")
        else:
            print(f"{chemical} is not a recognised acid yet") 


def check_peroxide(concentration):
    if concentration >allowed_peroxide_conc:
        print(f"{concentration} exceeds the allowed concencentration of {allowed_peroxide_conc} for liquid hydrogen peroxide.")
    else:
        print(f"{concentration} is within the allowed concentration of peroxide. You may proceed.")


regulated_chemicals = pd.read_csv("OSHA regulated chemicals.csv")
regulated_chemicals["OSHA regulated chemicals"] = regulated_chemicals["OSHA regulated chemicals"].str.lower().str.strip()
disallowed_list = regulated_chemicals["OSHA regulated chemicals"].to_list()

def check_disallowed(chemical):
    if chemical.lower() in disallowed_list:
        print(f"{chemical} is disallowed as per OSHA. You may not proceed.")
    else:
        print(f"{chemical} may be used")


def check_chemical(chemical, concentration):
    if chemical.lower() in disallowed_list:
        check_disallowed(chemical)
    elif chemical.lower() == "hydrogen peroxide":
        check_peroxide(concentration)
    elif chemical.lower() in banned or chemical.lower() in limits:
        check_acid(chemical, concentration)
    else:
        print(f"no rules for {chemical} yet")


check_chemical("Sulfuric Acid", 0.4)
check_chemical("nitric acid", 0.05)
check_chemical("Benzene", 0)
check_chemical("Hydrogen Peroxide", 0.35)
check_chemical("water", 0.1)