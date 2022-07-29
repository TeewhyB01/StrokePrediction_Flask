from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn
import pandas as pd
app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index2.html')
    else:
        predictformat = {
            'age': [],
            'hypertension':[],
            'heart_disease':[],
            'avg_glucose_level':[],
            'bmi':[],
            'gender_Male':[],
            'ever_married_Yes': [],
            'work_type_Private':[],
            'work_type_Never_worked':[],
            'work_type_Self-employed':[],
            'work_type_children':[],
            'Residence_type_Urban':[],
            'smoking_status_formerly smoked':[],
            'smoking_status_never smoked':[],
            'smoking_status_smokes':[]
        }
        age = request.form['age']
        age = int(age)
        hypertension = request.form['hypertension']
        heart_disease = request.form['HeartDisease']
        gender = request.form['gender']
        married = request.form['married']
        worktype = request.form['worktype']
        areatype = request.form['areatype']
        smokes = request.form['smokes']
        range = request.form['range']
        range = float(range)
        glucose = request.form['glucose']
        glucose = float(glucose)
        hypertension_class_no = 0
    
        heartDisease_class_no = 0
        
        
        
        if hypertension == 'Yes':
            hypertension_class_no = 1
        else:
            hypertension_class_no = 0
        
        if heart_disease == 'Yes':
            heartDisease_class_no = 1
        else:
            heartDisease_class_no = 0
        predictformat['age'].append(age)
        predictformat['hypertension'].append(hypertension_class_no)
        predictformat['heart_disease'].append(heartDisease_class_no)
        predictformat['avg_glucose_level'].append(glucose)
        predictformat['bmi'].append(range)
        if gender == 'Male':
            predictformat['gender_Male'].append(1)
        else:
            predictformat['gender_Male'].append(0)
        if married == 'Yes':
            predictformat['ever_married_Yes'].append(1)
        else: 
            predictformat['ever_married_Yes'].append(0)
        if worktype == 'Private':
            predictformat['work_type_Private'].append(1)
            predictformat['work_type_Never_worked'].append(0)
            predictformat['work_type_Self-employed'].append(0)
            predictformat['work_type_children'].append(0)
        elif worktype == 'Self-Employed':
            predictformat['work_type_Private'].append(0)
            predictformat['work_type_Never_worked'].append(0)
            predictformat['work_type_Self-employed'].append(1)
            predictformat['work_type_children'].append(0)
        elif worktype == 'Govt_job':
            predictformat['work_type_Private'].append(0)
            predictformat['work_type_Never_worked'].append(0)
            predictformat['work_type_Self-employed'].append(0)
            predictformat['work_type_children'].append(0)
        elif worktype == 'children':
            predictformat['work_type_Private'].append(0)
            predictformat['work_type_Never_worked'].append(0)
            predictformat['work_type_Self-employed'].append(0)
            predictformat['work_type_children'].append(1)
        elif worktype == 'Never Worked':
            predictformat['work_type_Private'].append(0)
            predictformat['work_type_Never_worked'].append(1)
            predictformat['work_type_Self-employed'].append(0)
            predictformat['work_type_children'].append(0)
        if areatype == 'Urban':
            predictformat['Residence_type_Urban'].append(1)
        else:
            predictformat['Residence_type_Urban'].append(0)
        if smokes == 'formerly_smoked':
            predictformat['smoking_status_formerly smoked'].append(1)
            predictformat['smoking_status_never smoked'].append(0)
            predictformat['smoking_status_smokes'].append(0)
        elif smokes == 'smokes':
            predictformat['smoking_status_formerly smoked'].append(0)
            predictformat['smoking_status_never smoked'].append(0)
            predictformat['smoking_status_smokes'].append(1)  
        elif smokes == 'never_smoked':
            predictformat['smoking_status_formerly smoked'].append(0)
            predictformat['smoking_status_never smoked'].append(1)
            predictformat['smoking_status_smokes'].append(0)
        predictformatDF = pd.DataFrame(predictformat,index=[0])
        file = 'RFStrokeModel.sav'
        model = pickle.load(open(file,'rb'))
        hiim = np.array(list(predictformat.values()))
        mylist =list(predictformat.values())
        prediction = model.predict(list(predictformat.values()))
        if prediction == 1:
            predictionvalue = "Your risk of getting a stroke is very high"
        else:
            predictionvalue = "You're healthy"
        return render_template('index2.html',minput=predictionvalue)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # file = 'RFStrokeModel.sav'
    # model = pickle.load(open(file,'rb'))
    # predictformat = {
    #     'age': 67,
    #     'hypertension':1,
    #     'heart_disease':1,
    #     'avg_glucose_level':86.0,
    #     'bmi':26.0,
    #     'gender_Male':1,
    #     'ever_married_Yes': 1,
    #     'work_type_Private':1,
    #     'work_type_Never_worked':0,
    #     'work_type_Self-employed':0,
    #     'work_type_children':0,
    #     'Residence_type_Urban':1,
    #     'smoking_status_formerly smoked':0,
    #     'smoking_status_never smoked':0,
    #     'smoking_status_smokes':1
    # }
    # prediction = model.predict([list(predictformat.values())])
    # # preds_as_str = str(prediction)
    # # print(preds_as_str)
    # # print(list(predictformat.values()))
    # return render_template('index.html')