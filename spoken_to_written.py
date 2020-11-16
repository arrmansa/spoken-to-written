def filter_text(text):
    #Replace
    replace_list = [('zero','0'),('one','1'),('two','2'),('three','3'),('four','4'),
                    ('five','5'),('six','6'),('seven','7'),('eight','8'),('nine','9'),('ten','10')]
    for i in range(len(replace_list)):
        while text.find(replace_list[i][0]) != -1:
            head, sep1, tail = text.partition(replace_list[i][0])
            text = head + replace_list[i][1] + tail
            
    #Condition for Double
    while text.find("Double ") != -1:
            head, sep1, tail = text.partition("Double ")
            word, _ , tail = tail.partition(" ")
            text = head + word + word + tail
            
    #Condition for Triple
    while text.find("Triple ") != -1:
            head, sep1, tail = text.partition("Triple ")
            word, _ , tail = tail.partition(" ")
            text = head + word + word + word + tail
            
    return(text)
