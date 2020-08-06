from flask import Flask, request, render_template
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__, template_folder='template')
model2=open('churn.pkl','rb')
light = pickle.load(model2)



@app.route("/")
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        # Total Stops
        SeniorCitizen = int(request.form["SeniorCitizen"])
        # print(Total_stops)
        tenure = int(request.form["tenure"])
        MonthlyCharges = float(request.form["MonthlyCharges"])
        TotalCharges = float(request.form["TotalCharges"])
        
        
        gender_Male=request.form['gender_Male']
        if(gender_Male=='Male'):
            
            gender_Male=1
        else:
            
            gender_Male=0
        
        Partner_Yes=request.form['Partner_Yes']
        if(Partner_Yes=='Yes'):
            Partner_Yes=1
        else:
            Partner_Yes=0
            
        Dependents_Yes=request.form['Dependents_Yes']
        if(Dependents_Yes=='Yes'):
            Dependents_Yes=1
        else:
            Dependents_Yes=0
            
        PhoneService_Yes=request.form['PhoneService_Yes']
        if(PhoneService_Yes=='Yes'):
            PhoneService_Yes=1
        else:
            PhoneService_Yes=0
        
         
        MultipleLines_Yes=request.form['MultipleLines_Yes']
        if(MultipleLines_Yes=='Yes'):
            MultipleLines_Yes=1
            MultipleLines_No_phone_service=0

        elif(MultipleLines_Yes=='No phone service'):
            MultipleLines_Yes=0
            MultipleLines_No_phone_service=1
        else:
            MultipleLines_Yes=0
            MultipleLines_No_phone_service=0
            
           
        OnlineBackup_Yes=request.form['OnlineBackup_Yes']
        if(OnlineBackup_Yes=='Yes'):
            OnlineBackup_Yes=1
            OnlineBackup_No_internet_service=0

        elif(OnlineBackup_Yes=='No internet service'):
            OnlineBackup_Yes=0
            OnlineBackup_No_internet_service=1
        else:
            OnlineBackup_Yes=0
            OnlineBackup_No_internet_service=0
            
        OnlineSecurity_Yes=request.form['OnlineSecurity_Yes']
        if(OnlineSecurity_Yes=='Yes'):
            OnlineSecurity_Yes=1
            OnlineSecurity_No_internet_service=0

        elif(OnlineSecurity_Yes=='No internet service'):
            OnlineSecurity_Yes=0
            OnlineSecurity_No_internet_service=1
        else:
            OnlineSecurity_Yes=0
            OnlineSecurity_No_internet_service=0 
            
        DeviceProtection_Yes=request.form['DeviceProtection_Yes']
        if(DeviceProtection_Yes=='Yes'):
            DeviceProtection_Yes=1
            DeviceProtection_No_internet_service=0

        elif(DeviceProtection_Yes=='No internet service'):
            DeviceProtection_Yes=0
            DeviceProtection_No_internet_service=1
        else:
            DeviceProtection_Yes=0
            DeviceProtection_No_internet_service=0
            
        TechSupport_Yes=request.form['TechSupport_Yes']
        if(TechSupport_Yes=='Yes'):
            TechSupport_Yes=1
            TechSupport_No_internet_service=0

        elif(TechSupport_Yes=='No internet service'):
            TechSupport_Yes=0
            TechSupport_No_internet_service=1
        else:
            TechSupport_Yes=0
            TechSupport_No_internet_service=0
            
        StreamingTV_Yes=request.form['StreamingTV_Yes']
        if(StreamingTV_Yes=='Yes'):
            StreamingTV_Yes=1
            StreamingTV_No_internet_service=0

        elif(StreamingTV_Yes=='No internet service'):
            StreamingTV_Yes=0
            StreamingTV_No_internet_service=1
        else:
            StreamingTV_Yes=0
            StreamingTV_No_internet_service=0
            
        StreamingMovies_Yes=request.form['StreamingMovies_Yes']
        if(StreamingMovies_Yes=='Yes'):
            StreamingMovies_Yes=1
            StreamingMovies_No_internet_service=0

        elif(StreamingMovies_Yes=='No internet service'):
            StreamingMovies_Yes=0
            StreamingMovies_Nointernet_service=1
        else:
            StreamingMovies_Yes=0
            StreamingMovies_No_internet_service=0
            
        
        Contract_One_year=request.form['Contract_One year']
        if(Contract_One_year=='One year'):
            Contract_One_year=1
            Contract_Two_year=0

        elif(Contract_One_year=='Two year'):
            Contract_One_year=0
            Contract_Two_year=1
        else:
            Contract_One_year=0
            Contract_Two_year=0
        
        PaperlessBilling_Yes=request.form['PaperlessBilling_Yes']
        if(PaperlessBilling_Yes=='Yes'):
            
            PaperlessBilling_Yes=1
        else:
            
            PaperlessBilling_Yes=0

        InternetService_No=request.form['InternetService_No']
        if(InternetService_No=='No'):
            InternetService_No=1
            InternetService_Fiber_optic=0

        elif(InternetService_No=='Fiber Optic'):
            InternetService_No=0
            InternetService_Fiber_optic=1
        else:
            InternetService_No=0
            InternetService_Fiber_optic=0     

            

            
            
            

 
        PaymentMethod_Creditcardautomatic=request.form['PaymentMethod_Creditcard(automatic)']
        if(PaymentMethod_Creditcardautomatic=='Creditcard(automatic)'):
            PaymentMethod_Creditcardautomatic=1
            PaymentMethod_Electroniccheck=0
            PaymentMethod_Mailedcheck=0
        elif(PaymentMethod_Creditcardautomatic=='Electroniccheck'):
            PaymentMethod_Creditcardautomatic=0
            PaymentMethod_Electroniccheck=1
            PaymentMethod_Mailedcheck=0
        elif(PaymentMethod_Creditcardautomatic=='Mailedcheck'):
            PaymentMethod_Creditcardautomatic=0
            PaymentMethod_Electroniccheck=0
            PaymentMethod_Mailedcheck=1
        else:
            PaymentMethod_Creditcardautomatic=0
            PaymentMethod_Electroniccheck=0
            PaymentMethod_Mailedcheck=0


        
        output=light.predict([[SeniorCitizen,tenure,MonthlyCharges,TotalCharges,
        gender_Male,Partner_Yes,Dependents_Yes,PhoneService_Yes,
        MultipleLines_No_phone_service,MultipleLines_Yes,
        OnlineBackup_No_internet_service,OnlineBackup_Yes,
        InternetService_Fiber_optic,InternetService_No,
        OnlineSecurity_No_internet_service,OnlineSecurity_Yes,
        DeviceProtection_No_internet_service,DeviceProtection_Yes,
        TechSupport_No_internet_service,TechSupport_Yes,
        StreamingTV_No_internet_service,StreamingTV_Yes,
        StreamingMovies_No_internet_service,StreamingMovies_Yes,
        Contract_One_year,Contract_Two_year,PaperlessBilling_Yes,
        PaymentMethod_Creditcardautomatic,
        PaymentMethod_Electroniccheck,PaymentMethod_Mailedcheck         
        ]])

        if output==0:
            res_val='not churned'
        else:
            res_val='churned'

        return render_template('home.html',prediction_text="the customer has {}".format(res_val))

    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run()
