# for example 
# physics data base 
# [physics,equations,equations,physics,maxwell,equations]
# [equations,physics,maxwell]
# [2/6      ,   3/6 , 1/6   ]

# math data base 
# [equations,integrals,euler,formulas,integrals,addition]
# [equations,integrals,euler,formulas,addition]
# [1/6      , 2/6     , 1/6 , 1/6    , 1/6    ]

# --> input i love reading about maxwell equations 
# (physics data base test)
# ==0+0+0+0+1/6+2/6=3/6=1/2

# (Math test)
# =0+0+0+0+0+1/6=1/6

# then we have 2 values 1/2 and 1/6 
# lets find their sum 
# =4/6

# physics match probability = (1/2) / (4/6) = 3/4=75%
# math match probability  =(1/6)/(4/6)=1/4=25%

# physics match is larger than math match then that talk is on physics

def remove_numbers(input_list):
    return [item for item in input_list if not isinstance(item, (int, float))]

file1=input("please enter the file names ")
file2=input("please enter the file names ")
file3=input("please enter the file names ")
file4=input("please enter the file names ")

f1=open(file1,'r')
f2=open(file2,'r')
f3=open(file3,'r')
f4=open(file4,'r')

numbers = list(range(10001))
numbers=[str(num) for num in numbers]
common_words=['important','good','better','nice']
stop_words = [
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren\'t', 'as', 'at', 
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can\'t', 'cannot', 'could', 
    'couldn\'t', 'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during', 'each', 'few', 'for', 
    'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 'having', 'he', 'he\'d', 'he\'ll', 'he\'s', 
    'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'how\'s', 'i', 'i\'d', 'i\'ll', 'i\'m', 
    'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 'it', 'it\'s', 'its', 'itself', 'let\'s', 'me', 'more', 'most', 'mustn\'t', 
    'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 
    'ourselves', 'out', 'over', 'own', 'same', 'shan\'t', 'she', 'she\'d', 'she\'ll', 'she\'s', 'should', 'shouldn\'t', 
    'so', 'some', 'such', 'than', 'that', 'that\'s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 
    'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve', 'this', 'those', 'through', 'to', 'too', 
    'under', 'until', 'up', 'very', 'was', 'wasn\'t', 'we', 'we\'d', 'we\'ll', 'we\'re', 'we\'ve', 'were', 'weren\'t', 
    'what', 'what\'s', 'when', 'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 'who\'s', 'whom', 'why', 'why\'s', 
    'with', 'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll', 'you\'re', 'you\'ve', 'your', 'yours', 
    'yourself', 'yourselves','.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', '-', '...', '/', '\\', 
    '&', '*', '#', '$', '%', '+', '-', '=', '>', '<','—','a','b','c','d','e','e','f','g','h','i','j','k','l','m','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
stop_words.append(numbers)
stop_words.append(common_words)

encodings = ['utf-8', 'latin1', 'cp1252']
for encoding in encodings:
    try:
        with open(file1, encoding=encoding) as f1:
            sub1_sentence=f1.read()
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")
else:
    print("Could not read the file with any of the tested encodings.")

sub1_splitted=sub1_sentence.split()
sub1_splitted=[word.lower() for word in sub1_splitted]
sub1_words=[x for x in sub1_splitted if x not in stop_words]
sub1_prob=[(sub1_words.count(word)/len(sub1_words)) for word in sub1_words]

sub1_words_updated=[]
    
for word in sub1_words:
    if word not in sub1_words_updated:
        sub1_words_updated.append(word)
    else :
        continue
    
sub1_prob_updated=[]
for word in sub1_words_updated:
    sub1_prob_updated.append(sub1_prob[sub1_words.index(word)])
    


for encoding in encodings:
    try:
        with open(file2, encoding=encoding) as f2:
            sub2_sentence=f2.read()
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")
else:
    print("Could not read the file with any of the tested encodings.")
    

 

sub2_splitted=sub2_sentence.split()
sub2_splitted=[word.lower() for word in sub2_splitted]
sub2_words=[x for x in sub2_splitted if x not in stop_words]
sub2_prob=[(sub2_words.count(word)/len(sub2_words)) for word in sub2_words]

sub2_words_updated=[]
    
for word in sub2_words:
    if word not in sub2_words_updated:
        sub2_words_updated.append(word)
    else :
        continue
    
sub2_prob_updated=[]
for word in sub2_words_updated:
    sub2_prob_updated.append(sub2_prob[sub2_words.index(word)])
    
for encoding in encodings:
    try:
        with open(file3, encoding=encoding) as f3:
            sub3_sentence=f3.read()
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")
else:
    print("Could not read the file with any of the tested encodings.")    
    
sub3_splitted=sub3_sentence.split()
sub3_splitted=[word.lower() for word in sub3_splitted]
sub3_words=[x for x in sub3_splitted if x not in stop_words]
sub3_prob=[(sub3_words.count(word)/len(sub3_words)) for word in sub3_words]

sub3_words_updated=[]
    
for word in sub3_words:
    if word not in sub3_words_updated:
        sub3_words_updated.append(word)
    else :
        continue
    
sub3_prob_updated=[]
for word in sub3_words_updated:
    sub3_prob_updated.append(sub3_prob[sub3_words.index(word)])

for encoding in encodings:
    try:
        with open(file4, encoding=encoding) as f4:
            sub4_sentence=f4.read()
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")
else:
    print("Could not read the file with any of the tested encodings.")


sub4_splitted=sub4_sentence.split()
sub4_splitted=[word.lower() for word in sub4_splitted]
sub4_words=[x for x in sub4_splitted if x not in stop_words]
sub4_prob=[(sub4_words.count(word)/len(sub4_words)) for word in sub4_words]

sub4_words_updated=[]
    
for word in sub4_words:
    if word not in sub4_words_updated:
        sub4_words_updated.append(word)
    else :
        continue
    
sub4_prob_updated=[]
for word in sub4_words_updated:
    sub4_prob_updated.append(sub4_prob[sub4_words.index(word)])

f1.close()
f2.close()
f3.close()
f4.close()
    
 
test_sentence=input("Enter test sentence to test ")
test_splitted=test_sentence.split()
test_splitted=[word.lower() for word in test_splitted]
test_words=[x for x in test_splitted if x not in stop_words]

sum1=0
sum2=0
sum3=0
sum4=0

for word in test_words:
    for w in sub1_words_updated:
        if word in w:
            sum1=sum1+sub1_prob_updated[sub1_words_updated.index(w)]
        else:
            sum1=sum1  
    for w in sub2_words_updated:
        if word in w:          
            sum2=sum2+sub2_prob_updated[sub2_words_updated.index(w)]
        else:
            sum2=sum2 
    for w in sub3_words_updated:        
        if word in w:
            sum3=sum3+sub3_prob_updated[sub3_words_updated.index(w)]
        else:
            sum3=sum3 
    for w in sub4_words_updated:        
        if word in w:
            sum4=sum4+sub4_prob_updated[sub4_words_updated.index(w)]
        else:
            sum4=sum4
sum=sum1+sum2+sum3+sum4        
print((sum1/sum)*100,'%',(sum2/sum)*100,'%',(sum3/sum)*100,'%',(sum4/sum)*100,'%')


    
print('\n')

if (sum1>sum2 and sum1>sum3 and sum1 >sum4):
    #print("Talking about --> ",sub1_words_updated[sub1_prob_updated.index(max(sub1_prob_updated))])
    print("Talking about --> PHYSICS ")
    if (sum1/sum)>0.5:
            f1=open("sub1",'a')
            f1.write(test_sentence)
            f1.close()
            print("approved and added to sub1")
    else:
            print("was not added")
               
elif (sum2>sum1 and sum2>sum3 and sum2 >sum4): 
    #print("Talking about --> ",sub2_words_updated[sub2_prob_updated.index(max(sub2_prob_updated))])
    print("Talking about--> MATH")
    if (sum2/sum)>0.5:
        f2=open("sub2",'a')
        f2.write(test_sentence)
        f2.close()
        print("approved and added to sub2")
    else:
        print("was not added")
                
elif (sum3>sum1 and sum3>sum4 and sum3 >sum2):  
    #print("Talking about-->",sub3_words_updated[sub3_prob_updated.index(max(sub3_prob_updated))])
    print("Talking about--> Biology")
    if (sum3/sum)>0.5:
        f3=open("sub3",'a')
        f3.write(test_sentence)
        f3.close()
        print("approved and added to sub3")
         
    else:
        print("was not added")
                
elif (sum4>sum1 and sum4>sum2 and sum4 >sum3): 
   # print("Talking about --> ",sub4_words_updated[sub4_prob_updated.index(max(sub4_prob_updated))])
    print("Talking about --> History ")
    if (sum4/sum)>0.5:
        f4=open("sub4",'a')
        f4.write(test_sentence)
        f4.close()
        print("approved and added to sub4")
         
    else:
        print("was not added")
          
else :
    print("could not detect")
    
print('\n')
