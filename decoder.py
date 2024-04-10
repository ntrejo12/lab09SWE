def decoder(password):
    decode = []
    for i in range(len(password)):
        new_digit = int(password[i]) - 3
        decode.append(str(new_digit))

    final_decode = ''.join(decode)
    return final_decode