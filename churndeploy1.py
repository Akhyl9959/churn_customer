import numpy as np
import streamlit as st
import pickle


model = pickle.load(open("C:/Users/USER/Downloads/churn_model2.pkl","rb")) #loading the created model


st.set_page_config(page_title="CHURN MODEL APPLICATION") #tab title

#prediction function
def predict_status(AGE, CUS_Month_Income, CUS_Gender, CUS_Marital_Status,YEARS_WITH_US, totaldebitamount,totaldebittransactions,totalcreditamount, totalcredittransactions, CUS_Target,TAR_Desc):
    input_data =np.asarray ([AGE, CUS_Month_Income, CUS_Gender, CUS_Marital_Status,
           YEARS_WITH_US, totaldebitamount, totaldebittransactions,
           totalcreditamount, totalcredittransactions, CUS_Target,
           TAR_Desc])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("CHURN MODEL APPLICATION")
    st.write("A quick ML app to classify churn_customer and No Churn_customer ")

    #getting the input
    AGE= st.text_input("Enter your AGE")
    CUS_Month_Income = st.text_input("Enter your CUS_Month_Income")
    CUS_Gender = st.text_input("Enter your CUS_Gender")
    CUS_Marital_Status = st.text_input("Enter your CUS_Marital_Status")
    YEARS_WITH_US = st.text_input("Enter your YEARS_WITH_US")
    totaldebitamount = st.text_input("Enter your totaldebitamount")
    totaldebittransactions = st.text_input("Enter your totaldebittransactions")
    totalcreditamount = st.text_input("Enter your totalcreditamount")
    totalcredittransactions = st.text_input("Enter your totalcredittransactions")
    CUS_Target = st.text_input("Enter your CUS_Target")
    TAR_Desc = st.text_input("Enter your TAR_Desc")




    #predict value
    classification =" "

    if st.button("Predict"):
        classification = predict_status(AGE, CUS_Month_Income, CUS_Gender, CUS_Marital_Status,
               YEARS_WITH_US, totaldebitamount,totaldebittransactions,
               totalcreditamount,totalcredittransactions, CUS_Target,
               TAR_Desc)
        if classification==1:
            
            st.info("ACTIVE CUSTOMER")
            #st.markdown("![You're like this!](https://i.gifer.com/L6m.gif)")
        elif classification==0:
            st.info(" CHURN CUSTOMER")
                #st.markdown("![You're like this!](https://i.gifer.com/L6m.gif)")

        
        else:            
            st.error("noooo")

          
     
        
        
    st.write("## Thank you for Visiting \nProject by AKHIL CHETTI")
        #st.markdown("<h1 style='text-align: right; color: blue; font-size: small;'><a href='https://github.com/suyog56/CANCER'>Looking for Source Code?</a></h1>", unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: right; color: white; font-size: small'>you can find it on my GitHub</h1>", unsafe_allow_html=True)



if __name__=="__main__":
    main()
