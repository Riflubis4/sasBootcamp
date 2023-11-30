def is_palindrome(kata):
    N = len(kata)
    for i in range(1, N + 1):
        if kata[i - 1] != kata[N - i]:
            return False
    return True

while True:
    N = int(input("Masukkan panjang string: "))
    kata = input("Masukkan string: ")

    if is_palindrome(kata):
        print(f"{kata} True.")
    else:
        print(f"{kata} False.")

#if is_palindrome(kata):
    #print("True")
#else:
    #print("False")
