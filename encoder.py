def encoder(password):
    new_pass = []
    for num in password:
        int_num = int(num)
        int_num += 3
        str_num = str(int_num)
        new_pass.append(str_num)
    encode_pass = ''.join(new_pass)
    return encode_pass
