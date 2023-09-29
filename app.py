from flask import Flask, render_template, request, redirect, url_for
from src.Risk_Analysis.Pipeline.PredictionPipeline import CustomPipeline, PredictPipeline
from src.Risk_Analysis import logger

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_data():
    if request.method == 'POST':
        data = CustomPipeline(
            Term=request.form.get('Term'),
            NoEmp=request.form.get('NoEmp'),
            NewExist=request.form.get('NewExist'),
            CreateJob=request.form.get('CreateJob'),
            RetainedJob=request.form.get('RetainedJob'),
            UrbanRural=request.form.get('UrbanRural'),
            RevLineCr=request.form.get('RevLineCr'),
            LowDoc=request.form.get('LowDoc'),
            DisbursementGross=request.form.get('DisbursementGross'),
            GrAppv=request.form.get('GrAppv'),
            SBA_Appv=request.form.get('SBA_Appv')
        )
    
        logger.info("The data_frame_started")

        pred_df = data.get_the_data()

        data = PredictPipeline()

        res = data.predict_the_data(pred_df)
        print(res)

        print(pred_df)

        # Redirect to a new page with the results
        return render_template('results.html', results=res[0])

    # If the request method is GET, display the form page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)







