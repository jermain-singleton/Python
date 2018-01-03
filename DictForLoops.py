acro1 = ['Jean', 'Eren', 'Miska', 'Blu']
acro2 = ['Andre', 'Newton', 'Mikah', 'Jean', 'Eren']
for name in acro1:
    for name1 in acro2:
        if name1 not in acro1:
            print("Adding " + name1)
            acro1.append(name1)
for name in acro1:
    print(name)

# acro3 = {'skill1': 'cartwheel',
#          'skill2': 'headstand',
#          'skill3': 'chair',
#          'skill4': 'OAHS',
#        }

# for k, v in acro3.items():
#     print("skill: " + v)
# for k in acro3.keys():
#     print(k)
# for v in acro3.values():
#     print(v)