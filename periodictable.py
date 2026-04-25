import sqlite3

# ----------------------- DATABASE SETUP -----------------------
def create_database():
    try:
        conn = sqlite3.connect("periodic_table.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS elements_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                atomic_number INTEGER,
                symbol TEXT,
                name TEXT,
                mass TEXT,
                electronegativity TEXT,
                block TEXT,
                period TEXT
            )
        """)
        conn.commit()
        return conn, cur
    except Exception as e:
        print("Database creation error:", e)
        return None, None

def save_to_database(cur, conn, v, symbol, name, mass, elec, block, period):
    try:
        cur.execute("""
            INSERT INTO elements_log 
            (atomic_number, symbol, name, mass, electronegativity, block, period)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (v, symbol, name, mass, elec, block, period))
        conn.commit()
    except Exception as e:
        print("Error saving to database:", e)

# --------------------------------------------------------------
# ----------------------- START PROGRAM ------------------------
# --------------------------------------------------------------

print("::::::WELCOME TO WORLD OF PERIODIC TABLE:::::")
print("---HERE YOU CAN LEARN AND EXPAND YOUR KNOWLEDGE---")
print("USE : (A)YES , (B)NO") 

conn, cur = create_database()

D = input("DO YOU WANT TO CONTINUE THIS JOURNEY :").upper()

if D != "A":
    print("OPPS!!!")
    print("THIS WAS ALL ABOUT THESE INTERESTING ELEMENTS")
    print("--HAVE A NICE DAY--")
    quit()

print("         COME ON!!! ")
print("LET'S KNOW ABOUT 118 ELEMENTS")

# -------------------- DATA ARRAYS -------------------------
# original data (unchanged)
n1=["Hydrogen","Helium","Lithium","Berilliyum","Boron","Carbon","Nitrogen","Oxygen","Fluorine"]
n2=["Neon","Sodium","Magnesium","Aluminium","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium"]
n3=["Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobal","Nickel","Copper"]
n4=["Zinc","Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium"]
n5=["Zirconium","Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium"]
n6=["Tin","Antimony","Tellurium","Iodine","Xenon","Caesium","Barium","Lanthanum","Cerium","Praseodymium"]
n7=["Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","dysprosium","Holimium","Erbium","Thulium"]
n8=["ytterbium","Lutetium","Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold"]
n9=["Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium","Actinium"]
n10=["Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium"]
n11=["Fermium","Mendelevium","Nobelium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium"]
n12=["Darmstadtium","Roentgenium","Copernicium","Nihonium","Flerovium","Moscovium","Livermorium","Tennessine","Ogsnesson"]

m1=[1.008,4.003,6.941,9.012,10.811,12.011,14.007,15.999,18.998]
m2=[20.180,22.990,24.305,26.982,28.086,30.974,32.066,35.453,39.948,39.098]
m3=[40.078,44.956,47.867,50.942,51.996,54.938,55.845,58.933,58.693,63.546]
m4=[65.38,69.723,72.631,74.922,78.971,79.904,84.798,84.468,87.62,88.906]
m5=[91.224,92.906,95.95,98.907,101.07,102.906,106.42,107.868,112.414,114.818]
m6=[118.711,121.760,126.7,126.904,131.294,132.905,137.328,138.905,140.116,140.908]
m7=[144.243,144.913,150.36,151.964,157.25,158.925,162.500,164.930,167.259,168.934]
m8=[173.055,174.967,178.49,180.948,183.84,186.207,190.23,192.217,195.085,196.967]
m9=[200.592,204.383,207.2,208.980,208.982,209.987,222.081,223.020,226.025,227.028]
m10=[232.038,231.036,238.029,237,244,243,247,247,251,252]
m11=[257,258,259,262,261,262,266,264,269,268]
m12=[271,272,285,284,289,288,292,294,294]

sy1=['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F']
sy2=['NE','NA','MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K']
sy3=['CA','SC', 'TI','V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU']
sy4=['ZN','GA', 'GE','AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y']
sy5=['ZR','NB', 'MO','TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN']
sy6=['SN','SB', 'TE','I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR']
sy7=['ND','PM', 'SM','EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM']
sy8=['YB','LU', 'HF','TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU']
sy9=['HG','TL', 'PB','BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC']
sy10=['TH','PA', 'U','NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES']
sy11=['FM','MD', 'NO','LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT']
sy12=['DS','RG', 'CN','NH', 'FL', 'MC', 'LV', 'TS', 'OG']

e1=[2.2,"no data",0.98,1.57,2.04,2.55,3.04,3.44,3.98]
e2=["no data",0.93,1.31,1.61,1.9,2.19,2.58,3.16,"no data",0.82]
e3=[1,1.36,1.54,1.63,1.66,1.55,1.83,1.88,1.91,1.9]
e4=[1.65,1.81,2.01,2.18,2.55,2.96,3,0.82,0.95,1.22]
e5=[1.33,1.6,2.16,1.9,2.2,2.28,2.2,1.93,1.69,1.78]
e6=[1.96,2.05,2.1,2.66,2.6,0.79,0.89,1.1,1.12,1.13]
e7=[1.14,1.13,1.17,1.2,1.2,1.22,1.23,1.24,1.24,1.25]
e8=[1.1,1.27,1.3,1.5,2.36,1.9,2.2,2.2,2.28,2.54]
e9=[2,1.62,2.33,2.02,2,2.2,"no data",0.7,0.89,1.1]
e10=[1.3,1.5,1.38,1.36,1.28,1.3,1.3,1.3,1.3,1.3]
e11=[1.3,1.3,1.3,"no data","no data","no data","no data","no data","no data","no data"]
e12=["no data","no data","no data","no data","no data","no data","no data","no data","no data"]

# -------------------- MAIN LOOP ----------------------------

while True:
    try:
        v = int(input("\nEnter Atomic Number (1–118), or 0 to exit: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if v == 0:
        print("THANK YOU FOR USING THE PERIODIC TABLE!")
        break

    if v < 1 or v > 118:
        print("Atomic number must be between 1–118.")
        continue

    # Determine data section
    z = v // 10   # group
    y = v % 10
    if y == 0: y = 9

    # Select correct arrays
    data_groups = [
        (n1, sy1, m1, e1),
        (n2, sy2, m2, e2),
        (n3, sy3, m3, e3),
        (n4, sy4, m4, e4),
        (n5, sy5, m5, e5),
        (n6, sy6, m6, e6),
        (n7, sy7, m7, e7),
        (n8, sy8, m8, e8),
        (n9, sy9, m9, e9),
        (n10, sy10, m10, e10),
        (n11, sy11, m11, e11),
        (n12, sy12, m12, e12),
    ]

    group_index = min(z, 11)
    names, symbols, masses, electroneg = data_groups[group_index]

    name = names[y - 1]
    symbol = symbols[y - 1]
    mass = masses[y - 1]
    elec = electroneg[y - 1]

    print("\nSymbol: ", symbol)
    print("ELEMENT NAME :", name)

    # Asking what to display
    q = input("YOU CAN ASK: (A) ATOMIC MASS, (B) ELECTRONEGATIVITY, (C) BOTH: ").upper()

    if q == "A":
        print("ATOMIC MASS:", mass)
    elif q == "B":
        print("ELECTRONEGATIVITY:", elec)
    elif q == "C":
        print("ATOMIC MASS:", mass)
        print("ELECTRONEGATIVITY:", elec)
    else:
        print("Invalid choice, skipping extra data.")

    # Block & Period (simple classification)
    if symbol in ["H", "HE", "LI", "BE", "NA", "MG", "K", "CA", "RB", "SR", "CS", "BA", "FR", "RA"]:
        block = "S"
    elif symbol in ["SC", "TI", "V", "CR", "MN", "FE", "CO", "NI", "CU", "ZN"]:
        block = "D"
    else:
        block = "P"

    print("BLOCK:", block)

    # Simple Period determination
    if v <= 2: period = "1"
    elif v <= 10: period = "2"
    elif v <= 18: period = "3"
    elif v <= 36: period = "4"
    elif v <= 54: period = "5"
    elif v <= 86: period = "6"
    else: period = "7"

    print("PERIOD:", period)

    # Save to database
    save_to_database(cur, conn, v, symbol, name, mass, elec, block, period)

    print("Saved to database.")

print("Program Ended Successfully.")
