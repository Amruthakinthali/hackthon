from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


# Route to display the Eye Health Assessment form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form
    age = form_data['age']
    gender = form_data['gender']
    family_history = form_data['family_history']
    # Add other variables to capture form data based on column names in the database

    screen_time = form_data['screen_time']
    eye_strain_symptoms = request.form.getlist('eye_strain_symptoms')
    visual_acuity = form_data['visual_acuity']
    color_vision = form_data['color_vision']
    eye_protection = form_data['eye_protection']
    eye_injuries_surgeries = form_data['eye_injuries_surgeries']
    visual_field = form_data['visual_field']
    contact_lens_use = form_data['contact_lens_use']
    eye_health_habits = request.form.getlist('eye_health_habits')
    physical_activity = form_data['physical_activity']
    dietary_habits = form_data['dietary_habits']
    eye_alignment = form_data['eye_alignment']
    vision_changes = form_data['vision_changes']
    dry_eye_symptoms = form_data['dry_eye_symptoms']
    sleep_quality = form_data['sleep_quality']

    
  
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='eye'
    )
    cursor = conn.cursor()

    # Assuming you have a table named 'eye_health_assessment'
    query = f"""
        SELECT prevention 
        FROM eye_health_assessment 
        WHERE age = {age} AND 
        gender = '{gender}' AND 
        family_history = '{family_history}' AND
        screen_time = {screen_time} AND 
       
        visual_acuity = '{visual_acuity}' AND 
        color_vision = '{color_vision}' AND 
        eye_protection = '{eye_protection}' AND 
      
        visual_field = '{visual_field}' AND 
        contact_lens_use = '{contact_lens_use}' AND 
        
        physical_activity = {physical_activity} AND 
        dietary_habits = '{dietary_habits}' AND 
        eye_alignment = '{eye_alignment}' AND 
        vision_changes = '{vision_changes}' AND 
        dry_eye_symptoms = '{dry_eye_symptoms}' AND 
        sleep_quality = {sleep_quality}
  
    """
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Convert the result into a list of prevention items
    prevention_list = result[0] if result else "Protect your eyes from bright lights; Consume foods rich in antioxidants like blueberries and green leafy vegetables."


    conn.close()

    return render_template('result.html', prevention_list=prevention_list)

if __name__ == '__main__':
    app.run(debug=True)
