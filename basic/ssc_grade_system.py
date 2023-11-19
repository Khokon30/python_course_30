
bangla1 = 82
bangla2 = 84
english1 = 75
english2 = 71
overall_bangla = 166
overall_english = 146
general_math = 95
accounting = 88
business_organization_and_management = 72
finance_and_banking = 75
production_management_and_marketing = 86
principles_of_marketing = 90
comercial_geography_and_environment = 68
economics = 95
business_entrepreneurship = 85
ict = 90



print("Bangla1-",bangla1)   
print("Bangla2-",bangla2)
print("English1-",english1)
print("English2-",english2)
print("General Math-", general_math)
print("Accounting-",accounting)
print("Business Organization and Management-",business_organization_and_management)
print("Finance and Banking-",finance_and_banking)
print("Production Management and Marketing-",production_management_and_marketing)
print("Principles of Marketing-",principles_of_marketing)
print("Comercial Geography and Environment-",comercial_geography_and_environment)
print("Economics-",economics)
print("Business Entrepreneurship-",business_entrepreneurship)
print("ICT-",ict)




total_score = bangla1 + bangla2 + english1 + english2 + general_math + accounting + business_organization_and_management + finance_and_banking + production_management_and_marketing + principles_of_marketing + comercial_geography_and_environment + economics + business_entrepreneurship + ict
average_score = total_score /14 
print("Your total score is",total_score)
print("Your average score is",average_score)







if(bangla1<33 or bangla1>100 or bangla2<33 or bangla2>100 or english1<33 or english1>100 or english2<33 or english2>100 or general_math<33 or general_math>100 or accounting<33 or accounting>100 or business_organization_and_management<33 or business_organization_and_management>100 or finance_and_banking<33 or finance_and_banking>100 or production_management_and_marketing<33 or production_management_and_marketing>100 or principles_of_marketing<33 or principles_of_marketing>100 or comercial_geography_and_environment<33 or comercial_geography_and_environment>100 or economics<33 or economics>100 or business_entrepreneurship<33 or business_entrepreneurship>100 or ict<33 or ict>100  ):
    print("Invalid")

else:
    if(bangla1>=80):
        print("You have achieved GPA 5.00 in Bangla1 and your Grade is A+.")
    elif bangla1>=70:
        print("You have achieved GPA 4.00 in Bangla1 and your Grade is A.")
    elif bangla1>=60:
        print("You have achieved GPA 3.50 in Bangla1 and your Grade is A-.")
    elif bangla1>=50:
        print("You have achieved GPA 3.00 in Bangla1 and your Grade is B.")
    elif bangla1>=40:
        print("You have achieved GPA 2.00 in Bangla1  and your Grade is C.")
    elif bangla1>=33:
        print("You have achieved GPA 1.00 in Bangla1 and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Bangla1 and your Grade is F.")
    if(bangla2>=80):
        print("You have achieved GPA 5.00 in Bangla2 and your Grade is A+.")
    elif bangla2>=70:
        print("You have achieved GPA 4.00 in Bangla2 and your Grade is A.")
    elif bangla2>=60:
        print("You have achieved GPA 3.50 in Bangla2 and your Grade is A-.")
    elif bangla2>=50:
        print("You have achieved GPA 3.00 in Bangla2 and your Grade is B.")
    elif bangla2>=40:
        print("You have achieved GPA 2.00 in Bangla2  and your Grade is C.")
    elif bangla2>=33:
        print("You have achieved GPA 1.00 in Bangla2 and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Bangla2 and your Grade is F.")



    if(bangla1+bangla2>=160):
        print("You have achieved GPA 5.00 in Overall Bangla and your Grade is A+.")
    elif bangla1+bangla2>=140:
        print("You have achieved GPA 4.00 in Overall Bangla and your Grade is A.")
    elif bangla1+bangla2>=120:
        print("You have achieved GPA 3.50 in Overall Bangla and your Grade is A-.")
    elif bangla1+bangla2>=100:
        print("You have achieved GPA 3.00 in Overall Bangla and your Grade is B.")
    elif bangla1+bangla2>=80:
        print("You have achieved GPA 2.00 in Overall Bangla  and your Grade is C.")
    elif bangla1+bangla2>=66:
        print("You have achieved GPA 1.00 in Overall Bangla and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Overall Bangla and your Grade is F.")





    if(english1>=80):
        print("You have achieved GPA 5.00 in English1 and your Grade is A+.")
    elif english1>=70:
        print("You have achieved GPA 4.00 in English1 and your Grade is A.")
    elif english1>=60:
        print("You have achieved GPA 3.50 in English1 and your Grade is A-.")
    elif english1>=50:
        print("You have achieved GPA 3.00 in English1 and your Grade is B.")
    elif english1>=40:
        print("You have achieved GPA 2.00 in English1 and your Grade is C.")
    elif english1>=33:
        print("You have achieved GPA 1.00 in English1 and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in English1 and your Grade is F.")





    if(english2>=80):
        print("You have achieved GPA 5.00 in English2 and your Grade is A+.")
    elif english2>=70:
        print("You have achieved GPA 4.00 in English2 and your Grade is A.")
    elif english2>=60:
        print("You have achieved GPA 3.50 in English2 and your Grade is A-.")
    elif english2>=50:
        print("You have achieved GPA 3.00 in English2 and your Grade is B.")
    elif english2>=40:
        print("You have achieved GPA 2.00 in English2 and your Grade is C.")
    elif english2>=33:
        print("You have achieved GPA 1.00 in English2 and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in English2 and your Grade is F.")




    if(english1+english2>=160):
        print("You have achieved GPA 5.00 in Overall English and your Grade is A+.")
    elif english1+english2>=140:
        print("You have achieved GPA 4.00 in Overall English and your Grade is A.")
    elif english1+english2>=120:
        print("You have achieved GPA 3.50 in Overall English and your Grade is A-.")
    elif english1+english2>=100:
        print("You have achieved GPA 3.00 in Overall English and your Grade is B.")
    elif english1+english2>=80:
        print("You have achieved GPA 2.00 in Overall English and your Grade is C.")
    elif english1+english2>=66:
        print("You have achieved GPA 1.00 in Overall English and your Grade is D.") 
    else:
        print("You have achieved GPA 0.00 in Overall English and your Grade is F.")




    if(general_math>=80):
        print("You have achieved GPA 5.00 in General Math and your Grade is A+.")
    elif general_math>=70:
        print("You have achieved GPA 4.00 in General Math and your Grade is A.") 
    elif general_math>=60:
        print("You have achieved GPA 3.50 in General Math and your Grade is A-.") 
    elif general_math>=50:
        print("You have achieved GPA 3.00 in General Math and your Grade is B.") 
    elif general_math>=40:
        print("You have achieved GPA 2.00 in General Math and your Grade is C.")
    elif general_math>=33:
        print("You have achieved GPA 1.00 in General Math and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in General Math and your Grade is F.")




    if(accounting>=80):
        print("You have achieved GPA 5.00 in Accounting and your Grade is A+.")
    elif accounting>=70:
        print("You have achieved GPA 4.00 in Accounting and your Grade is A.")
    elif accounting>=60:
        print("You have achieved GPA 3.50 in Accounting and your Grade is A-.")
    elif accounting>=50:
        print("You have achieved GPA 3.00 in Accounting and your Grade is B.")
    elif accounting>=40:
        print("You have achieved GPA 2.00 in Accounting and your Grade is C.")
    elif accounting>=33:
        print("You have achieved GPA 1.00 in Accounting and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Accounting and your Grade is F.")





    if(business_organization_and_management>=80):
        print("You have achieved GPA 5.00 in Business Organization and Management and your Grade is A+.")
    elif business_organization_and_management>=70:
        print("You have achieved GPA 4.00 in Business Organization and Management and your Grade is A.")
    elif business_organization_and_management>=60:
        print("You have achieved GPA 3.50 in Business Organization and Management and your Grade is A-.")
    elif business_organization_and_management>=50:
        print("You have achieved GPA 3.00 in Business Organization and Management and your Grade is B.")
    elif business_organization_and_management>=40:
        print("You have achieved GPA 2.00 in Business Organization and Management and your Grade is C.")
    elif business_organization_and_management>=33:
        print("You have achieved GPA 1.00 in Business Organization and Management and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Business Organization and Management and your Grade is F.")






    if(finance_and_banking>=80):
        print("You have achieved GPA 5.00 in Finance and Banking and your Grade is A+.")
    elif finance_and_banking>=70:
        print("You have achieved GPA 4.00 in Finance and Banking and your Grade is A.")
    elif finance_and_banking>=60:
        print("You have achieved GPA 3.50 in Finance and Banking and your Grade is A-.")
    elif finance_and_banking>=50:
        print("You have achieved GPA 3.00 in Finance and Banking and your Grade is B.")
    elif finance_and_banking>=40:
        print("You have achieved GPA 2.00 in Finance and Banking and your Grade is C.")
    elif finance_and_banking>=33:
        print("You have achieved GPA 1.00 in Finance and Banking and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Finance and Banking and your Grade is F.")





    if(production_management_and_marketing>=80):
        print("You have achieved GPA 5.00 in Production Management and Marketing and your Grade is A+.")
    elif production_management_and_marketing>=70:
        print("You have achieved GPA 4.00 in Production Management and Marketing and your Grade is A.")
    elif production_management_and_marketing>=60:
        print("You have achieved GPA 3.50 in Production Management and Marketing and your Grade is A-.")
    elif production_management_and_marketing>=50:
        print("You have achieved GPA 3.00 in Production Management and Marketing and your Grade is B.")
    elif production_management_and_marketing>=40:
        print("You have achieved GPA 2.00 in Production Management and Marketing and your Grade is C.")
    elif production_management_and_marketing>=33:
        print("You have achieved GPA 1.00 in Production Management and Marketing and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Production Management and Marketing and your Grade is F.")






    if(principles_of_marketing>=80):
        print("You have achieved GPA 5.00 in Principles of Marketing and your Grade is A+.")
    elif principles_of_marketing>=70:
        print("You have achieved GPA 4.00 in Principles of Marketing and your Grade is A.")
    elif principles_of_marketing>=60:
        print("You have achieved GPA 3.50 in Principles of Marketing and your Grade is A-.")
    elif principles_of_marketing>=50:
        print("You have achieved GPA 3.00 in Principles of Marketing and your Grade is B.")
    elif principles_of_marketing>=40:
        print("You have achieved GPA 2.00 in Principles of Marketing and your Grade is C.")
    elif principles_of_marketing>=33:
        print("You have achieved GPA 1.00 in Principles of Marketing and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Principles of Marketing and your Grade is F.")






    if(comercial_geography_and_environment>=80):
        print("You have achieved GPA 5.00 in Comercial Geography and Environment and your Grade is A+.")
    elif comercial_geography_and_environment>=70:
        print("You have achieved GPA 4.00 in Comercial Geography and Environment and your Grade is A.")
    elif comercial_geography_and_environment>=60:
        print("You have achieved GPA 3.50 in Comercial Geography and Environment and your Grade is A-.")
    elif comercial_geography_and_environment>=50:
        print("You have achieved GPA 3.00 in Comercial Geography and Environment and your Grade is B.")
    elif comercial_geography_and_environment>=40:
        print("You have achieved GPA 2.00 in Comercial Geography and Environment and your Grade is C.")
    elif comercial_geography_and_environment>=33:
        print("You have achieved GPA 1.00 in Comercial Geography and Environment and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Comercial Geography and Environment and your Grade is F.")






    if(economics>=80):
        print("You have achieved GPA 5.00 in Economics and your Grade is A+.")
    elif economics>=70:
        print("You have achieved GPA 4.00 in Economics and your Grade is A.")
    elif economics>=60:
        print("You have achieved GPA 3.50 in Economics and your Grade is A-.")
    elif economics>=50:
        print("You have achieved GPA 3.00 in Economics and your Grade is B.")
    elif economics>=40:
        print("You have achieved GPA 2.00 in Economics and your Grade is C.")
    elif economics>=33:
        print("You have achieved GPA 1.00 in Economics and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Economics and your Grade is F.")






    if(business_entrepreneurship>=80):
        print("You have achieved GPA 5.00 in Business Entrepreneurship and your Grade is A+.")
    elif business_entrepreneurship>=70:
        print("You have achieved GPA 4.00 in Business Entrepreneurship and your Grade is A.")
    elif business_entrepreneurship>=60:
        print("You have achieved GPA 3.50 in Business Entrepreneurship and your Grade is A-.")
    elif business_entrepreneurship>=50:
        print("You have achieved GPA 3.00 in Business Entrepreneurship and your Grade is B.")
    elif business_entrepreneurship>=40:
        print("You have achieved GPA 2.00 in Business Entrepreneurship and your Grade is C.")
    elif business_entrepreneurship>=33:
        print("You have achieved GPA 1.00 in Business Entrepreneurship and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in Business Entrepreneurship and your Grade is F.")







    if(ict>=80):
        print("You have achieved GPA 5.00 in ICT and your Grade is A+.")
    elif ict>=70:
        print("You have achieved GPA 4.00 in ICT and your Grade is A.")
    elif ict>=60:
        print("You have achieved GPA 3.50 in ICT and your Grade is A-.")
    elif ict>=50:
        print("You have achieved GPA 3.00 in ICT and your Grade is B.")
    elif ict>=40:
        print("You have achieved GPA 2.00 in ICT and your Grade is C.")
    elif ict>=33:
        print("You have achieved GPA 1.00 in ICT and your Grade is D.")
    else:
        print("You have achieved GPA 0.00 in ICT and your Grade is F.")













            


                                                                           

                


