 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier-knn imputated.pkl', 'rb') 


classifier = pickle.load(pickle_in)


 
def prediction(Gender,Married,Education,Self_Employed,ApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        if Gender == "Male":
            Gender = 0
        else:
            Gender = 1
 
        if Married == "Unmarried":
            Married = 0
        else:
            Married = 1
 
        if Credit_History == "Unclear Debts":
            Credit_History = 0
        else:
            Credit_History = 1

        if Education == "Graduate":
            Education = 0
        else:
           Education = 1

        if Self_Employed == "Yes":
           Self_Employed = 1
        else:
           Self_Employed = 0  

        if Property_Area == "Rural":
           Property_Area = 0

        if Property_Area == 'Urban':
           Property_Area = 2

        else:
           Property_Area = 1 
        
        LoanAmount = LoanAmount 
        Loan_Amount_Term = Loan_Amount_Term 
        ApplicantIncome = ApplicantIncome
    
        prediction = classifier.predict(
            [[Gender,Married,Education,Self_Employed,ApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
     
        if prediction == 0:
           pred = 'Rejected'
        else:
           pred = 'Approved'
        
        print(prediction)
        return pred



def main():
    st.title('loan prediction')
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married"))
    Education =  st.selectbox('Education',("Graduate","Not Graduate"))
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    
    Self_Employed = st.selectbox('Self_Employed',('No','Yes'))
    Property_Area = st.selectbox('Property Location',('Urban','Rural','Semiurban'))
    Loan_Amount_Term = st.number_input("Loan Amount Term") 
    
    result = ""
    if st.button('Predict'):

        result = prediction(Gender,Married,Education,Self_Employed,ApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
    
    st.success('Your Loan Amount is {}'.format(result))

if __name__=='__main__':
    main()




      
