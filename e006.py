def check_char():
    word= input("Introduce una palabra: ")
    for char in word:
        if "@" == char:
            print("La palabra contiene el carácter @")
        elif "#" == char:
            print("La palabra contiene el carácter #")
        elif "$" == char:
            print("La palabra contiene el carácter $")
        elif "%" == char:
            print("La palabra contiene el carácter %")
        else:
            print("La palabra no contiene ninguno de los caracteres @, #, $ o %")