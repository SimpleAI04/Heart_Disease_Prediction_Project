from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Tạo ứng dụng Flask
app = Flask(__name__)

# Load mô hình RandomForest đã lưu
model = joblib.load('model_randomforest.pkl')

# Tạo trang web nhập dữ liệu
@app.route('/')
def home():
    return render_template('index.html')

# Xử lý dự đoán khi người dùng nhập dữ liệu
@app.route('/predict', methods=['POST'])
def predict():
    # Lấy dữ liệu từ form
    features = [float(x) for x in request.form.values()]
    
    # Chuyển dữ liệu thành DataFrame hoặc định dạng phù hợp
    columns = ['Age','RestingBP','Cholesterol','MaxHR','Oldpeak','Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope','FastingBS']
    data = pd.DataFrame([features], columns=columns)
    
    # Dự đoán bằng mô hình
    prediction = model.predict(data)
    
    # Trả kết quả dự đoán
    output = 'Có nguy cơ mắc bệnh tim' if prediction[0] == 1 else 'Không có nguy cơ mắc bệnh tim'
    
    return render_template('index.html', prediction_text=f'Kết quả dự đoán: {output}')

if __name__ == "__main__":
    app.run(debug=True)
