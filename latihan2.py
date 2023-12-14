def weight_conversion():
    berat = int(input("Masukkan berat badan : "))
    type = str(input("Lbs atau Kg : "))

    lbs = berat * 2.204623
    kg = berat * 0.453592

    if (type =="K"):
        print(f"berat badan adalah {kg}Kg")
    elif(type == "L"):
        print(f"berat badan adalah {lbs}Lbs")   