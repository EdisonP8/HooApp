encode = str.maketrans('eilouvy','1234567')#加密方式 
words = 'iloveyou' 
encode_words = words.translate(encode)#按encode加密方式加密 
print(encode_words) #输出23461745 
dedoed = str.maketrans('1234567','eilouvy')#解密方式 
dedoed_words = encode_words.translate(dedoed)#按decode解密方式解密 
print(dedoed_words)#输出iloveyou 