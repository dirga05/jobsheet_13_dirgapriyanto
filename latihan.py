def guess_number():
    secret_number = 9
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit :
        user = int(input("Gues : "))
        if user == secret_number :
            print("Anda berhasil")
            break
        else :
            print("Salah")
            guess_count = guess_count + 1

    else :
        print("Kesempatan Anda Habis")
