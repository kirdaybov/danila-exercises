def end_check(str):
    if str[-4:] == '.com':
        return True
    else:
        return False

test = 'ыловарр.com'

test2 = 'sdfjkh.dh'

supertest = end_check(test2)

if supertest == True:
    print("Вернул тру")
else:
    print('Вернул фолс')