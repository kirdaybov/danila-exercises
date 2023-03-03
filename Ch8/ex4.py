def morse_code_converter(text):
    text = str(text).replace(',','--..--')
    text = str(text).replace('0','-----')
    text = str(text).replace('А','.-')
    return text
test = input('Введите текст"А 0 А ,":\n')
text = morse_code_converter(test)
print(f'На азбуке Морзе это будет\n{text}')

#Решил не прописывать все знаки, чтобы не тратить время
