def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(ciphertext):
    m = ''
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if not ch.isalpha():
            m += ch
        else:
            c = to_identity_map(ch)
            m += from_identity_map(c - i)
    return m

encrypted_message = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"
decrypted_message = decrypt(encrypted_message)

print("Decrypted Message:")
print("HTB{" + decrypted_message + "}")