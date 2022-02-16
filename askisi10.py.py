#askisi_10
file= open ("two_cities_ascii.txt", "r")
text = file.read()
t_text = ""
for j in text:
    f1 = bin(ord(j))
    f1 = f1[2:].zfill(7)
    dig = f1[0:2] + f1[6:8]
    t_text =t_text + dig 
total_p , p_zygoi , p_3 , p_5 , p_7 = 0 , 0 , 0 , 0 , 0
for j in range(0,len(t_text),16):
    total_p = total_p + 1
    numb = int(t_text[j:j+16], 2)
    if numb % 2 == 0:
        p_zygoi = p_zygoi + 1
    if numb % 3 == 0:
        p_3 = p_3 + 1
    if numb % 5 == 0:
        p_5 = p_5 + 1
    if numb % 7 == 0:
        p_7 = p_7 + 1
pos_zygoi = p_zygoi/total_p*100
print("Oi zygoi einai: ",pos_zygoi ,"%")
pos_3 = p_3/total_p*100
print("Autoi pou diairountai me to 3 einai: ",pos_3 ,"%") 
pos_5 = p_5/total_p*100
print("Autoi pou diairountai me to 5 einai: ",pos_5 ,"%")
pos_7 = p_7/total_p*100
print("Autoi pou diairountai me to 7 einai:",pos_7 ,"%")
file.close()
"""metavlites:
    total_p=synoliko plithos arithmwn
    p_zygoi=plithos zygwn
    pos_zygoi=pososto zygwn
    p_3=plithos pou diairoyntai me to p_3
    pos_3=pososto pou diairoyntai me to 3
    p_5=plithos poy diairoyntai me to p_5
    pos_5=pososto pou diairoyntai me to 5
    p_7=plithos pou diairoyntai me to p_7
    pos_7=pososto pou diairoyntai me to 7
    t_text=akolouthia arithmwn apto ascii arxeio
    numb=arithmoi sto dekadiko
    dig=ta dyo prwta kai ta 2 teleytaia bits poy krataw

"""    
    
    
    
    
    
    
  