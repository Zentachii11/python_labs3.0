def insert_text_into_file(file_path, text, line_number):
    with open(file_path, 'r+', encoding='utf-8') as laba_file:
        line_count = sum(1 for _ in laba_file)

        if line_number < 1 or line_number > line_count + 1:
            print("Номер строки находится вне диапазона существующих строк.")
            return

        laba_file.seek(0)

        lines = laba_file.readlines()
        lines.insert(line_number - 1, text)

        laba_file.seek(0)
        laba_file.writelines(lines)


file_path = r"C:\Users\kalin\Desktop\пример.txt"
text_to_insert = "пример"
line_number_to_insert = 5
insert_text_into_file(file_path, text_to_insert, line_number_to_insert)
