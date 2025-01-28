from flask import Flask ,render_template,request
import pickle

app=Flask(__name__)

def prediction(lst):
    filename='model/loanpridict.pickle'
    with open(filename,'rb') as file:
        model=pickle.load(file)
    pred_val=model.predict([lst])
    return pred_val
    

@app.route('/',methods=['POST','GET'])

def index():
    pred=None
    if request.method=='POST':
        gender=request.form['gender']
        married=request.form['married']
        dependents=request.form['dependents']
        education=request.form['education']
        self_Employed=request.form['self_Employed']
        propertyarea=request.form['propertyarea']
        credithistory=request.form['credithistory']
        applicantIncome=request.form['applicantIncome']
        coapplicantIncome=request.form['coapplicantIncome']
        loanAmount=request.form['loanAmount']
        loanamountterm=request.form['loanamountterm']
        
        feature_list=[]
        feature_list.append(int(applicantIncome))
        feature_list.append(int(coapplicantIncome))
        feature_list.append(int(loanAmount))
        feature_list.append(float(loanamountterm))
        
        gender_list =['male','female']
        married_list=['married','single']
        dependents_list=['0','1','2','3','3+']
        education_list=['graduated','not graduated']
        self_Employed_list=['yes','no']
        propertyarea_list=['rural','urban','semiurban']
        credithistory_list=['0','10']
        
        def traverse(lst,value):
            for iteam in lst:
                if iteam==value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
                    
        traverse(gender_list,gender)
        traverse(married_list,married)
        traverse(dependents_list,dependents)
        traverse(education_list,education)
        traverse(self_Employed_list,self_Employed)
        traverse(propertyarea_list,propertyarea)
        traverse(credithistory_list,credithistory)
        
        pred =prediction(feature_list)
        
        
    
    
        
     
    return render_template('index.html',pred=pred)



if __name__=='__main__':
    app.run(debug=True)