def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Перевірка, чи символ є буквою
            if char.islower():  # Перевірка, чи символ є малою літерою
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            shifted_char = char

        encrypted_text += shifted_char

    return encrypted_text


def main():
    text = input("Введіть рядок для шифрування: ")

    while True:
        try:
            shift = int(input("Введіть значення зсуву (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Зсув повинен бути у діапазоні від 1 до 25.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    encrypted_text = caesar_cipher(text, shift)
    print(f"Закодований текст: {encrypted_text}")


if __name__ == "__main":
    main()
