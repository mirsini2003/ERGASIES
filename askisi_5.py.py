with open('two_cities_ascii.txt') as f:
    fin=f.read()
    fin_mic=fin.lower()
    lexeis=fin_mic.split()
    
    print('Οι 10 δημοφιλέστερες λέξεις είναι: ')
    for j in range (1,11):
        print(j,max(set(lexeis), key=lexeis.count))
        i=0
        while i<len(lexeis):
            if lexeis[i]==max(set(lexeis), key=lexeis.count):
                lexeis.remove(max(set(lexeis), key=lexeis.count))
            i+=1
        
    prwta_2_grammata=[x[:2] for x in lexeis]
    print('Οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι: ')
    for j in range (1,4):
        print(j,max(set(prwta_2_grammata), key=prwta_2_grammata.count))
        i=0
        while i<len(prwta_2_grammata):
            if prwta_2_grammata[i]==max(set(prwta_2_grammata), key=prwta_2_grammata.count):
                prwta_2_grammata.remove(max(set(prwta_2_grammata), key=prwta_2_grammata.count))
            i+=1
    
    prwta_3_grammata=[x[:3] for x in lexeis]
    print('Οι τρεις πρώτοι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι: ')
    for j in range (1,4):
        print(j,max(set(prwta_3_grammata), key=prwta_3_grammata.count))
        i=0
        while i<len(prwta_3_grammata):
            if prwta_3_grammata[i]==max(set(prwta_3_grammata), key=prwta_3_grammata.count):
                prwta_3_grammata.remove(max(set(prwta_3_grammata), key=prwta_3_grammata.count))
            i+=1


