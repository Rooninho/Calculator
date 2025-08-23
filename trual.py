# ward_4a = ['Bed1: Robert','Bed2: Josephine','Bed3: Asha']
# ward_4a.append('bed4: John')
# print(ward_4a)

# discharged=ward_4a.pop(3)
# print(f'{discharged} {ward_4a}')

# Turples

# emergency_exits=(
#     ("main lobby",1,12.5),
#     ("ER back",1,87.3),
#     ("ICU wing",3,45.0)
# )

# print("Exit near ICU wing:",emergency_exits[2][0])
# print('exit near main lobby:',emergency_exits[0][0])
# try:
#     emergency_exits[1]=('lab zone',2,34.5)
# except TypeError:
#     print('turples are immutable')


# dictionaries

# staff={
#   101: {"name": "DR Teddy","role": "surgeon","station": "all over"},
#   102: {"name": "DR Charity","role": "neurologist","station": 3},
#   103: {"name":"DR Faith","role":"pediatrician","station":2}
# }

# patients={
#     201: {"name": "Robert","ailment":"flu","ward":5},
#     202: {"name": "josephine","ailment":"fracture","ward":4}
# }

# print("Doctor on duty:", staff[102]['role'])
# print('patient in ward 4:',patients[202]["name"])

# sets

sterile_lab_equipment={'microscope','centrifuge',"bunsen burner"}
sterile_er_equipment={'defibrillator','oxygen tank','stethoscope'}

# contaminated equipments

contaminated={'stethoscope','defibrillator'}

# sterilize ER equipment
sterile_er_equipment=contaminated
print('sterile ER equipment:',sterile_er_equipment)