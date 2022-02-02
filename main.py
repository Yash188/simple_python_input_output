country = input("Enter your country name: ")

if country == 'India' :
    print("You are an Indian")
    age = int(input("Enter your age: "))
    if age >= 18 :
        print("You are eligible to vote at :"+str(age)+" age")
    else:
        print("You are not eligible to vote at :"+age+" age")
else :
    print("You are not an Indian")
    
        
