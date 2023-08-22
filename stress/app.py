from flask import Flask, render_template, request

app = Flask(__name__)

preventive_measures = {
    "regular-yes-regular-deep-breathing-controlled-yes-adequate-consistent-consulted": "Engage in regular deep breathing exercises and controlled screen time. Maintain a consistent exercise routine and engage in hobbies for relaxation. Seek professional help for stress management.",
    "irregular-yes-infrequent-meditation-uncontrolled-yes-limited-consistent-consulted": "Practice regular meditation and control your screen time. Although exercise is infrequent, make sure it's consistent when you do engage. Allocate limited time for relaxation activities. Seek professional help to manage stress.",
    "irregular-no-infrequent-deep-breathing-uncontrolled-no-limited-rarely-consulted": "Consider adopting a regular sleep schedule and deep breathing exercises. Reduce uncontrolled screen time and make sure to take breaks during work. Engage in relaxation hobbies more often and consult a professional for stress management.",
    "regular-yes-infrequent-listening-music-uncontrolled-no-adequate-rarely-consulted": "Use music for relaxation and stress relief. Although screen time is uncontrolled, you have adequate relaxation time. Engage in hobbies for relaxation more often and consider consulting a professional for further guidance.",
    "regular-yes-infrequent-meditation-controlled-no-adequate-consistent-not-consulted": "Continue practicing regular meditation and controlled screen time. Maintain consistent exercise and relaxation routines. While you haven't consulted a professional, consider seeking help for stress management.",
    # Add more entries based on the combinations of questionnaire responses
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sleep_schedule = request.form.get("sleepSchedule")
        work_breaks = request.form.get("workBreaks")
        exercise_routine = request.form.get("exerciseRoutine")
        relaxation_techniques = request.form.get("relaxationTechniques")
        screen_time_control = request.form.get("screenTimeControl")
        regular_exercise = request.form.get("regularExercise")
        time_relaxation = request.form.get("timeRelaxation")
        hobbies_relaxation = request.form.get("hobbiesRelaxation")
        professional_help = request.form.get("professionalHelp")

        user_input_key = "-".join([
            sleep_schedule, work_breaks, exercise_routine, relaxation_techniques,
            screen_time_control, regular_exercise, time_relaxation, hobbies_relaxation,
            professional_help
        ])

        preventive_measure = preventive_measures.get(user_input_key, "Practice regular meditation and control your screen time. Although exercise is infrequent, make sure it's consistent when you do engage. Allocate limited time for relaxation activities. Seek professional help to manage stress.")
        return render_template("result.html", preventive_measure=preventive_measure)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True,port=8080)
