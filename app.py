from flask import Flask, render_template, session, redirect, url_for, request
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

with open('static/data/questions.json', 'r', encoding='utf-8') as f:
    QUESTIONS = json.load(f)


@app.route('/')
def home():
    # 访问 Home 时，在 session 里打个标记
    session['show_hint'] = True
    return render_template('home_test.html')

@app.route('/iso')
def iso_page():
    # 只有 session 中有 show_hint 才把它弹一次，然后立刻清掉
    show_hint = session.pop('show_hint', False)
    return render_template('iso.html', show_hint=show_hint)

@app.route('/ss')
def shutter_speed_page():
    show_hint = session.pop('show_hint', False)
    return render_template('ss.html', show_hint=show_hint)

@app.route('/aperture')
def aperture_page():
    show_hint = session.pop('show_hint', False)
    return render_template('aperture.html', show_hint=show_hint)


@app.route('/simulator')
def simulator_page():
    return render_template('simulator.html')


# @app.route('/quiz')
# def quiz_page():
#     return render_template('quiz.html')

@app.route('/review', methods=['GET','POST'])
def review():
    # since it is required to store data for each page
    # for review page, I stored the entry timestamp
    history = session.get('history', [])
    # append a new entry — use isoformat() so it's JSON‐serializable
    history.append({
        'page':    'review',
        'entered_at': datetime.utcnow().isoformat()
    })
    session['history'] = history

    if request.method == 'POST':
        session['review_done'] = True
        return redirect(url_for('start_quiz'))
    return render_template('review.html')

@app.route("/quiz")
def quiz_home():
    return render_template("quiz_home.html", active="quiz")

@app.route('/start_quiz')
def start_quiz():
    session.clear()
    session['scores'] = [0]*len(QUESTIONS)
    session['score']  = 0
    session['answers'] = [None] * len(QUESTIONS)
    return redirect(url_for('quiz', q_num=1))

@app.route('/quiz/<int:q_num>', methods=['GET','POST'])
def quiz(q_num):
    total = len(QUESTIONS)
    
    if q_num > total:
        return redirect(url_for('quiz_result'))
    question = QUESTIONS[q_num-1]
    feedback = None

    if request.method == 'POST':
        process_answer(q_num-1, request.form)
        feedback = session.pop('feedback', None)
        return render_template(
            f'question{q_num}.html',
            question=question,
            feedback=feedback,
            score=session['score'],
            q_num=q_num
        )
    return render_template(
        f'question{q_num}.html',
        question=question,
        feedback=feedback,
        score=session['score'],
        q_num=q_num
    )


@app.route('/quiz/result')
def quiz_result():
    return render_template('quiz_base.html',
                           show_results=True,
                           score=session['score'],
                           answers=session.get('answers'))

def process_answer(q_num, form):
    feedback = None
    score_increment = 0

    if q_num == 0:  # ISO Question
        user_answer = form.get('answer')
        session['answers'][0] = user_answer
        correct = user_answer == str(QUESTIONS[0]['correct'])
        feedback = {
            'correct': correct,
            'message': QUESTIONS[0]['feedback']['correct'] if correct else QUESTIONS[0]['feedback']['incorrect']
        }
        session['scores'][0] = 1 if correct else 0

    elif q_num == 1:  # Shutter Speed Question
        user_answer = form.get('answer')
        session['answers'][1] = user_answer
        correct = user_answer == str(QUESTIONS[1]['correct'])
        feedback = {
            'correct': correct,
            'message': QUESTIONS[1]['options'][int(user_answer)]['feedback'] if user_answer else '',
            'correct_answer': QUESTIONS[1]['options'][QUESTIONS[1]['correct']]['text']
        }
        session['scores'][1] = 1 if correct else 0

    elif q_num == 2:  # Matching Question
        user_answers = []
        feedback     = []
        score_inc    = 0

        for i, sub_q in enumerate(QUESTIONS[2]["subquestions"]):
            raw = form.get(f"subq_{i}")          # radio value or None
            if raw is None:                      # user skipped
                user_answers.append(None)
                feedback.append({
                    "correct": False,
                    "user_answer": None,
                    "message": "Please choose an option.",
                    "correct_answer": sub_q["options"][sub_q["correct"]]["text"]
                })
                continue

            idx         = int(raw)               # index 0-2
            chosen_opt  = sub_q["options"][idx]
            correct_opt = sub_q["options"][sub_q["correct"]]["text"]
            correct     = idx == sub_q["correct"]
            if correct:
                score_inc += 1

            user_answers.append(idx)
            feedback.append({
                "correct":     correct,
                "user_answer": idx,
                "message":     chosen_opt["feedback"],   # ← comes straight from JSON
                "correct_answer": correct_opt
            })

        session["answers"][2] = user_answers
        session["scores"][2]  = score_inc

    if feedback is not None:
        session['feedback'] = feedback
    session['score'] = sum(session['scores'])



if __name__ == '__main__':
    app.run(debug=True)