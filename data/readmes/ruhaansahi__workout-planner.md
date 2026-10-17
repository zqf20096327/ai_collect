# Workout Builder

A workout planner. Pick your muscle groups, how long you've got, and
what equipment isn't available, and it builds a full session with
exercises, sets, reps, and rest, swapping in an alternative exercise
wherever a machine is missing.

Live: https://workout-planner-5x2vjgo5t-ruhaansahi-projects.vercel.app/

## Frontend

Plain HTML, CSS, and JavaScript — no framework. `index.html` holds the
form and layout, `styles.css` handles the styling, and `app.js` runs the
form logic and builds the session.

## ML model

`ml/build_model.py` uses scikit-learn to work out which exercises can
substitute for each other. Every exercise is encoded into a feature
vector based on its muscle group, secondary muscles, movement type, and
difficulty, using `OneHotEncoder` and `MultiLabelBinarizer`. A
`NearestNeighbors` model then finds, for each exercise, the closest
others that train the same muscle but use different equipment. Those
become its substitutes.

This runs offline, not live. It writes its output to
`data/exercises.json`, which is what the app actually reads in the
browser. Run it again whenever the exercise list changes:

```bash
python3 ml/build_model.py
```
