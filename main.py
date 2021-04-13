a = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

b = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

c = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }]

def getBMI(n):
    underWeight = 18.4
    minNormalWeight, maxNormalWeight = 18.5, 24.9
    minOverWeight, maxOverWeight = 25, 29.9
    minModObese, maxModObese = 30, 35.9
    minSevereObese, maxSevereObese = 35, 39.9
    verySevereObese = 40
    overWeightCount = 0
    doc = []
    print(type(underWeight))
    for i in a:
        gender = i["Gender"]
        heightM = i["HeightCm"]/100
        heightM = round(heightM, 1)
        weightKg = i["WeightKg"]
        myBMI = round(weightKg/heightM,1)
        print(myBMI)
        if myBMI<0:
            print("BMI data not Valid", myBMI)
        elif myBMI<underWeight:
            dicts = {"Underweight":{
                "BMI":myBMI,
                "Risk":"Malnutritioned"
            }}
            doc.append(dicts)
            print("Underweight - Malnutritioned", myBMI)
        elif minNormalWeight<myBMI<maxNormalWeight:
            print("Normal Weight - Risk Low")
            dicts = {"Normal_Weight":{
                "BMI":myBMI,
                "Risk":"Low Risk"
            }}
            doc.append(dicts)
        elif minOverWeight<myBMI<maxOverWeight:
            overWeightCount +=1
            dicts = {"Over_Weight":{
                "BMI":myBMI,
                "Risk":"Enhanced Risk"
            }}
            doc.append(dicts)
            print("OverWieght - Risk Enhanced", myBMI)
        elif minModObese<myBMI<maxModObese:
            overWeightCount +=1
            dicts = {"Moderately_Obese":{
                "BMI":myBMI,
                "Risk":"Medium Risk"
            }}
            doc.append(dicts)
            print("Moderately Obese - Risk Medium", myBMI)
        elif minSevereObese<myBMI<maxSevereObese:
            overWeightCount +=1
            dicts = {"Severe_Obese":{
                "BMI":myBMI,
                "Risk":"High Risk"
            }}
            doc.append(dicts)
            print("Severe Obese - Rish High", myBMI)
        elif myBMI>verySevereObese:
            overWeightCount +=1
            dicts = {"Sever_Obese":{
                "BMI":myBMI,
                "Risk":"Very_High_Risk"
            }}
            doc.append(dicts)
            print("Severe Obese - Very High Risk", myBMI)
        else:
            dicts = {"Not_Valid"}
            doc.append(dicts)
        dicts = {}
    print("Total Number of OverWeight People= ", overWeightCount)
    print(doc)
    return (doc)
if __name__ == "__main__":
    getBMI(a)
    getBMI(b)
    getBMI(c)


#Time - O(n)
#Space - O(n)