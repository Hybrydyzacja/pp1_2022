phone = {
    "brand": "Samsung",
    "model": "XYZ",
    "year": 2020,
    "battery mAh": 2500,
    "cool": True,
    "else": ["waterproof", "dustproof"]
}


for key, value in phone.items():
    print(key, "-", value)


# for key in phone.keys():    #jak samo for samo "key" to .keys() zamiast .items()
#     value = phone[key]    
#     print(key, "-", value)