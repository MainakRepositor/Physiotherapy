# This will be a web app using streamlit which will
# be an exercise database for clients to use

# Import libraries
import streamlit as st
import pandas as pd
from Muscle_Group_Pics import muscle_group_pics
from Exercise_Demo_Pics import demo_pics

df = pd.read_csv('Exercise Library - Exercises.csv')


equipment = ['Any', 'Atlas Stone', 'Barbell', 'Bodyweight',
             'Cable Machine', 'D-Ball', 'Dip Bars', 'Dumbbell', 
             'Exercise Ball', 'EZ Bar', 'Glute Ham Roller',
             'Kettlebell', 'Medicine Ball', 'Mini Band', 'Parallettes',
             'Plate', 'Pull-Up Bar', 'Resistance Band', 'Rings',
             'Rope', 'Sandbag', 'Slamball', 'Sled', 'Specialized Machine',
             'Trap Bar', 'Wrist Roller']

st.set_page_config(page_title='Physiotherapy', 
                   page_icon='🧑‍⚕️', 
                   layout='wide')

st.title('Physiotherapy Exerciser')

st.sidebar.header('⬇ Choose From Filters Below ⬇')

muscle_group = st.sidebar.radio('Primary Muscle Group:', options = ['All', 'Abdominals', 'Abductors', 
                                        'Adductors', 'Anterior Tibialis', 
                                        'Biceps', 'Calves', 'Chest', 
                                        'Forearms', 'Glutes', 'Hamstrings', 
                                        'Lats', 'Lower Back', 'Obliques', 
                                        'Quads', 'Shoulders', 
                                        'Shoulders (Rotator Cuff)', 
                                        'Traps', 'Triceps', 'Upper Back'])
if muscle_group == 'All':
    df = df
if muscle_group == 'Abdominals':
    df = df[df['Primary Muscle Group'] == 'Abdominals']
if muscle_group == 'Abductors':
    df = df[df['Primary Muscle Group'] == 'Abductors']
if muscle_group == 'Adductors':
    df = df[df['Primary Muscle Group'] == 'Adductors']
if muscle_group == 'Anterior Tibialis':
    df = df[df['Primary Muscle Group'] == 'Anterior Tibialis']
if muscle_group == 'Biceps':
    df = df[df['Primary Muscle Group'] == 'Biceps']
if muscle_group == 'Calves':
    df = df[df['Primary Muscle Group'] == 'Calves']
if muscle_group == 'Chest':
    df = df[df['Primary Muscle Group'] == 'Chest']
if muscle_group == 'Forearms':
    df = df[df['Primary Muscle Group'] == 'Forearms']  
if muscle_group == 'Glutes':
    df = df[df['Primary Muscle Group'] == 'Glutes']
if muscle_group == 'Hamstrings':
    df = df[df['Primary Muscle Group'] == 'Hamstrings']
if muscle_group == 'Lats':
    df = df[df['Primary Muscle Group'] == 'Lats']
if muscle_group == 'Lower Back':
    df = df[df['Primary Muscle Group'] == 'Lower Back']
if muscle_group == 'Obliques':
    df = df[df['Primary Muscle Group'] == 'Obliques']
if muscle_group == 'Quads':
    df = df[df['Primary Muscle Group'] == 'Quads']
if muscle_group == 'Shoulders':
    df = df[df['Primary Muscle Group'] == 'Shoulders']
if muscle_group == 'Shoulders (Rotator Cuff)':
    df = df[df['Primary Muscle Group'] == 'Shoulders (Rotator Cuff)']
if muscle_group == 'Traps':
    df = df[df['Primary Muscle Group'] == 'Traps']
if muscle_group == 'Triceps':
    df = df[df['Primary Muscle Group'] == 'Triceps']
if muscle_group == 'Upper Back':
    df = df[df['Primary Muscle Group'] == 'Upper Back']

start_diff, end_diff = st.sidebar.select_slider('Difficulty Level:',
                        options = [1, 2, 3, 4, 5],
                        value = (1, 5))

df = df[(df['Difficulty Level'] >= start_diff) & (df['Difficulty Level'] <= end_diff)]

equipment_type = st.sidebar.selectbox('Equipment Type:',
                                      options = equipment)

if equipment_type == 'Any':
    df = df
if equipment_type == 'Atlas Stone':
    df = df[df['Equipment Options'].str.contains('Atlas Stone')]
if equipment_type == 'Barbell':
    df = df[df['Equipment Options'].str.contains('Barbell')]
if equipment_type == 'Bodyweight':
    df = df[df['Equipment Options'].str.contains('Bodyweight')]
if equipment_type == 'Cable Machine':
    df = df[df['Equipment Options'].str.contains('Cable Machine')]
if equipment_type == 'D-Ball':
    df = df[df['Equipment Options'].str.contains('D-Ball')]
if equipment_type == 'Dip Bars':
    df = df[df['Equipment Options'].str.contains('Dip Bars')]
if equipment_type == 'Dumbbell':
    df = df[df['Equipment Options'].str.contains('Dumbbell')]
if equipment_type == 'Exercise Ball':
    df = df[df['Equipment Options'].str.contains('Exercise Ball')]
if equipment_type == 'EZ Bar':
    df = df[df['Equipment Options'].str.contains('EZ Bar')]
if equipment_type == 'Glute Ham Roller':
    df = df[df['Equipment Options'].str.contains('Glute Ham Roller')]
if equipment_type == 'Kettlebell':
    df = df[df['Equipment Options'].str.contains('Kettlebell')]
if equipment_type == 'Medicine Ball':
    df = df[df['Equipment Options'].str.contains('Medicine Ball')]
if equipment_type == 'Mini Band':
    df = df[df['Equipment Options'].str.contains('Mini Band')]
if equipment_type == 'Parallettes':
    df = df[df['Equipment Options'].str.contains('Parallettes')]
if equipment_type == 'Plate':
    df = df[df['Equipment Options'].str.contains('Plate')]
if equipment_type == 'Pull-Up Bar':
    df = df[df['Equipment Options'].str.contains('Pull-Up Bar')]
if equipment_type == 'Resistance Band':
    df = df[df['Equipment Options'].str.contains('Resistance Band')]
if equipment_type == 'Rings':
    df = df[df['Equipment Options'].str.contains('Rings')]
if equipment_type == 'Rope':
    df = df[df['Equipment Options'].str.contains('Rope')]
if equipment_type == 'Sandbag':
    df = df[df['Equipment Options'].str.contains('Sandbag')]
if equipment_type == 'Slamball':
    df = df[df['Equipment Options'].str.contains('Slamball')]
if equipment_type == 'Sled':
    df = df[df['Equipment Options'].str.contains('Sled')]
if equipment_type == 'Specialized Machine':
    df = df[df['Equipment Options'].str.contains('Specialized Machine')]
if equipment_type == 'Trap Bar':
    df = df[df['Equipment Options'].str.contains('Trap Bar')]
if equipment_type == 'Wrist Roller':
    df = df[df['Equipment Options'].str.contains('Wrist Roller')]

df = df.fillna('None')
st.dataframe(df)

column_1, column_2, column_3 = st.columns(3)

with column_1:
    checkbox_1 = st.checkbox('View Exercise Images', value = False)
with column_2:
    checkbox_2 = st.checkbox('Write Your Physiotherapy Exercises', value = False)

if checkbox_1:
    column_4, column_5 = st.columns(2)
    options = [''] + df['Name'].tolist()
    with column_4:
        selected_exercise = st.selectbox('Select Exercise:', options = options, index = 0)

    st.header('Muscles Affected')
    col_1, col_2, col_3 = st.columns(3)


    with col_1:
        if selected_exercise == 'Sit-Ups':
            st.image(muscle_group_pics[0], width = 200)
        if selected_exercise == 'G.H.D. Sit-Ups':
            st.image(muscle_group_pics[2], width = 200)
        if selected_exercise == 'Flutter Kicks':
            st.image(muscle_group_pics[4], width = 200)
        if selected_exercise == 'Lying Leg Raises':
            st.image(muscle_group_pics[6], width = 200)
        if selected_exercise == 'In & Outs':
            st.image(muscle_group_pics[8], width = 200)
        if selected_exercise == 'Scissor Kicks':
            st.image(muscle_group_pics[10], width = 200)
        if selected_exercise == 'Decline Sit-Ups':
            st.image(muscle_group_pics[12], width = 200)
        if selected_exercise == 'Decline Reverse Crunch':
            st.image(muscle_group_pics[14], width = 200)
        if selected_exercise == 'Hanging Knee Raises':
            st.image(muscle_group_pics[16], width = 200)
        if selected_exercise == 'Hanging Leg Raises':
            st.image(muscle_group_pics[18], width = 200)
        if selected_exercise == 'Toes-To-Bar':
            st.image(muscle_group_pics[20], width = 200)
        if selected_exercise == 'Dead Bugs':
            st.image(muscle_group_pics[22], width = 200)
        if selected_exercise == 'Lying Knee Tucks':
            st.image(muscle_group_pics[24], width = 200)
        if selected_exercise == 'Sit-Ups w/ Ball Toss':
            st.image(muscle_group_pics[26], width = 200)
        if selected_exercise == 'Knee Tuck Holds':
            st.image(muscle_group_pics[28], width = 200)
        if selected_exercise == 'Knee Tuck Planks':
            st.image(muscle_group_pics[30], width = 200)
        if selected_exercise == 'Planks':
            st.image(muscle_group_pics[32], width = 200)
        if selected_exercise == 'Side Step Planks':
            st.image(muscle_group_pics[34], width = 200)
        if selected_exercise == 'Lying Leg Circles':
            st.image(muscle_group_pics[36], width = 200)
        if selected_exercise == 'Ab Bicycle':
            st.image(muscle_group_pics[38], width = 200)
        if selected_exercise == 'Banana/Cannon Ball':
            st.image(muscle_group_pics[40], width = 200)
        if selected_exercise == 'Hollow Body Holds':
            st.image(muscle_group_pics[42], width = 200)
        if selected_exercise == 'Ball Slams':
            st.image(muscle_group_pics[44], width = 200)
        if selected_exercise == 'Stir-The-Pot':
            st.image(muscle_group_pics[46], width = 200)
        if selected_exercise == 'Sledgehammer Strikes':
            st.image(muscle_group_pics[48], width = 200)
        if selected_exercise == 'Roll-Outs':
            st.image(muscle_group_pics[50], width = 200)
        if selected_exercise == 'Kneeling Crunches':
            st.image(muscle_group_pics[52], width = 200)
        if selected_exercise == 'Lateral Band Walks':
            st.image(muscle_group_pics[54], width = 200)
        if selected_exercise == 'Standing Hip Abductions':
            st.image(muscle_group_pics[56], width = 200)
        if selected_exercise == 'Seated Hip Abductions':
            st.image(muscle_group_pics[58], width = 200)
        if selected_exercise == 'Side Lying Hip Abductions':
            st.image(muscle_group_pics[60], width = 200)
        if selected_exercise == 'Side Plank Clamshells':
            st.image(muscle_group_pics[62], width = 200)
        if selected_exercise == 'Copenhagen Plank':
            st.image(muscle_group_pics[64], width = 200)
        if selected_exercise == 'Seated Hip Adductions':
            st.image(muscle_group_pics[66], width = 200)
        if selected_exercise == 'Standing Hip Adductions':
            st.image(muscle_group_pics[68], width = 200)
        if selected_exercise == 'Adductor Leg Lifts':
            st.image(muscle_group_pics[70], width = 200)
        if selected_exercise == 'Shin Curls':
            st.image(muscle_group_pics[72], width = 200)
        if selected_exercise == 'Heel Walks':
            st.image(muscle_group_pics[74], width = 200)
        if selected_exercise == 'Hammer Curls':
            st.image(muscle_group_pics[76], width = 200)
        if selected_exercise == 'Seated Incline Bicep Curl':
            st.image(muscle_group_pics[78], width = 200)
        if selected_exercise == 'Bicep Curl':
            st.image(muscle_group_pics[80], width = 200)
        if selected_exercise == 'Preacher Curl':
            st.image(muscle_group_pics[82], width = 200)
        if selected_exercise == 'Rope Climbs':
            st.image(muscle_group_pics[84], width = 200)
        if selected_exercise == 'Jumping Rope':
            st.image(muscle_group_pics[86], width = 200)
        if selected_exercise == 'Calf Raises':
            st.image(muscle_group_pics[88], width = 200)
        if selected_exercise == 'Seated Calf Raises':
            st.image(muscle_group_pics[90], width = 200)
        if selected_exercise == 'Single-Leg Calf Raises':
            st.image(muscle_group_pics[92], width = 200)
        if selected_exercise == 'Chest Flys':
            st.image(muscle_group_pics[94], width = 200)
        if selected_exercise == 'Incline Chest Flys':
            st.image(muscle_group_pics[96], width = 200)
        if selected_exercise == 'Decline Chest Flys':
            st.image(muscle_group_pics[98], width = 200)
        if selected_exercise == 'Push-Ups':
            st.image(muscle_group_pics[100], width = 200)
        if selected_exercise == 'Bench Press':
            st.image(muscle_group_pics[102], width = 200)
        if selected_exercise == 'Incline Bench Press':
            st.image(muscle_group_pics[104], width = 200)
        if selected_exercise == 'Decline Bench Press':
            st.image(muscle_group_pics[106], width = 200)
        if selected_exercise == 'Squeeze Press':
            st.image(muscle_group_pics[108], width = 200)
        if selected_exercise == 'Floor Press':
            st.image(muscle_group_pics[110], width = 200)
        if selected_exercise == 'Kneeling Chest Pass':
            st.image(muscle_group_pics[112], width = 200)
        if selected_exercise == "Farmer's Walk":
            st.image(muscle_group_pics[114], width = 200)
        if selected_exercise == 'Wrist Roller':
            st.image(muscle_group_pics[116], width = 200)
        if selected_exercise == 'Standing Hip Extensions':
            st.image(muscle_group_pics[118], width = 200)
        if selected_exercise == 'Donkey Kicks':
            st.image(muscle_group_pics[120], width = 200)
        if selected_exercise == 'Hip Thrusters':
            st.image(muscle_group_pics[122], width = 200)
        if selected_exercise == 'Glute Drive Machine':
            st.image(muscle_group_pics[124], width = 200)
        if selected_exercise == 'Glute Bridges':
            st.image(muscle_group_pics[126], width = 200)
        if selected_exercise == 'Single-Leg Hip Thrusters':
            st.image(muscle_group_pics[128], width = 200)
        if selected_exercise == 'Single-Leg Glute Bridge':
            st.image(muscle_group_pics[130], width = 200)
        if selected_exercise == 'Single-Leg Pull Throughs':
            st.image(muscle_group_pics[132], width = 200)
        if selected_exercise == 'Shin Hops':
            st.image(muscle_group_pics[134], width = 200)
        if selected_exercise == 'Glute Ham Raises':
            st.image(muscle_group_pics[136], width = 200)
        if selected_exercise == 'Standing Leg Curls':
            st.image(muscle_group_pics[138], width = 200)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(muscle_group_pics[140], width = 200)
        if selected_exercise == 'Kettlebell Swings':
            st.image(muscle_group_pics[142], width = 200)
        if selected_exercise == 'Romanian Deadlift':
            st.image(muscle_group_pics[144], width = 200)
        if selected_exercise == 'Single-Leg Romanian Deadlift':
            st.image(muscle_group_pics[146], width = 200)
        if selected_exercise == 'Good Mornings':
            st.image(muscle_group_pics[148], width = 200)
        if selected_exercise == 'Air Runner (Self-Powered Treadmill)':
            st.image(muscle_group_pics[150], width = 200)
        if selected_exercise == 'Snatch High Pull':
            st.image(muscle_group_pics[152], width = 200)
        if selected_exercise == 'Clean High Pull':
            st.image(muscle_group_pics[154], width = 200)
        if selected_exercise == 'Snatch Pull':
            st.image(muscle_group_pics[156], width = 200)
        if selected_exercise == 'Clean Pull':
            st.image(muscle_group_pics[158], width = 200)
        if selected_exercise == 'Lying Leg Curls (Floor)':
            st.image(muscle_group_pics[160], width = 200)
        if selected_exercise == 'Lying Leg Curls (Machine)':
            st.image(muscle_group_pics[162], width = 200)
        if selected_exercise == 'Banded Marches':
            st.image(muscle_group_pics[164], width = 200)
        if selected_exercise == 'Chin-Ups':
            st.image(muscle_group_pics[166], width = 200)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(muscle_group_pics[168], width = 200)
        if selected_exercise == 'Pull-Ups':
            st.image(muscle_group_pics[170], width = 200)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(muscle_group_pics[172], width = 200)
        if selected_exercise == 'Lat Pulldown':
            st.image(muscle_group_pics[174], width = 200)
        if selected_exercise == 'Neutral-Grip Lat Pulldown':
            st.image(muscle_group_pics[176], width = 200)
        if selected_exercise == 'Single-Arm Lat Pulldown':
            st.image(muscle_group_pics[178], width = 200)
        if selected_exercise == 'Chin-Up Grip Lat Pulldown':
            st.image(muscle_group_pics[180], width = 200)
        if selected_exercise == 'Pull-Overs':
            st.image(muscle_group_pics[182], width = 200)
        if selected_exercise == 'Ski Erg':
            st.image(muscle_group_pics[184], width = 200)
        if selected_exercise == 'Straight-Arm Lat Pulldown':
            st.image(muscle_group_pics[186], width = 200)
        if selected_exercise == 'Back Extensions':
            st.image(muscle_group_pics[188], width = 200)
        if selected_exercise == 'Reverse Hypers':
            st.image(muscle_group_pics[190], width = 200)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(muscle_group_pics[192], width = 200)
        if selected_exercise == 'Bird Dog':
            st.image(muscle_group_pics[194], width = 200)
        if selected_exercise == 'Deadlift':
            st.image(muscle_group_pics[196], width = 200)
        if selected_exercise == 'Supermans':
            st.image(muscle_group_pics[198], width = 200)
        if selected_exercise == 'Lying Heel Touches':
            st.image(muscle_group_pics[200], width = 200)
        if selected_exercise == 'Windshield Wipers':
            st.image(muscle_group_pics[202], width = 200)
        if selected_exercise == 'Hanging Oblique Knee Raises':
            st.image(muscle_group_pics[204], width = 200)
        if selected_exercise == 'Pallof Press Holds':
            st.image(muscle_group_pics[206], width = 200)
        if selected_exercise == 'Pallof Press':
            st.image(muscle_group_pics[208], width = 200)
        if selected_exercise == 'Russian Twists':
            st.image(muscle_group_pics[210], width = 200)
        if selected_exercise == 'Hanging Windshield Wipers':
            st.image(muscle_group_pics[212], width = 200)
        if selected_exercise == 'Around-The-Worlds':
            st.image(muscle_group_pics[214], width = 200)
        if selected_exercise == 'Side Bends':
            st.image(muscle_group_pics[216], width = 200)
        if selected_exercise == "Single-Arm Farmer's Walk":
            st.image(muscle_group_pics[218], width = 200)
        if selected_exercise == 'Side Planks':
            st.image(muscle_group_pics[220], width = 200)
        if selected_exercise == 'Side Plank Pulses':
            st.image(muscle_group_pics[222], width = 200)
        if selected_exercise == 'Lateral Ball Throws':
            st.image(muscle_group_pics[224], width = 200)
        if selected_exercise == 'Lateral Ball Slams':
            st.image(muscle_group_pics[226], width = 200)
        if selected_exercise == 'Standing High-To-Low Twist':
            st.image(muscle_group_pics[228], width = 200)
        if selected_exercise == 'Shoulder Taps':
            st.image(muscle_group_pics[230], width = 200)
        if selected_exercise == 'Contact Twists':
            st.image(muscle_group_pics[232], width = 200)
        if selected_exercise == 'Box Jumps':
            st.image(muscle_group_pics[234], width = 200)
        if selected_exercise == 'Depth Jumps':
            st.image(muscle_group_pics[236], width = 200)
        if selected_exercise == 'Depth Drops':
            st.image(muscle_group_pics[238], width = 200)
        if selected_exercise == 'Hurdle Jumps':
            st.image(muscle_group_pics[240], width = 200)
        if selected_exercise == 'Broad Jumps':
            st.image(muscle_group_pics[242], width = 200)
        if selected_exercise == 'Explosive Step-Ups':
            st.image(muscle_group_pics[244], width = 200)
        if selected_exercise == 'Lateral Hurdle Jumps':
            st.image(muscle_group_pics[246], width = 200)
        if selected_exercise == 'Bike Erg':
            st.image(muscle_group_pics[248], width = 200)
        if selected_exercise == 'Stairmaster':
            st.image(muscle_group_pics[250], width = 200)
        if selected_exercise == 'Speed Skater Jumps':
            st.image(muscle_group_pics[252], width = 200)
        if selected_exercise == 'Sled Push':
            st.image(muscle_group_pics[254], width = 200)
        if selected_exercise == 'Plyo Lunges':
            st.image(muscle_group_pics[256], width = 200)
        if selected_exercise == 'Reverse Sled Drag':
            st.image(muscle_group_pics[258], width = 200)
        if selected_exercise == 'Lateral Lunges':
            st.image(muscle_group_pics[260], width = 200)
        if selected_exercise == 'Lateral Sled Drag':
            st.image(muscle_group_pics[262], width = 200)
        if selected_exercise == 'Leg Press':
            st.image(muscle_group_pics[264], width = 200)
        if selected_exercise == 'Single-Leg Leg Press':
            st.image(muscle_group_pics[266], width = 200)
        if selected_exercise == 'Reverse Lunges':
            st.image(muscle_group_pics[268], width = 200)
        if selected_exercise == 'Box Squats':
            st.image(muscle_group_pics[270], width = 200)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(muscle_group_pics[272], width = 200)
        if selected_exercise == 'Foot Elevated Reverse Lunges':
            st.image(muscle_group_pics[274], width = 200)
        if selected_exercise == 'Single-Leg Box Squats':
            st.image(muscle_group_pics[276], width = 200)
        if selected_exercise == 'Pistol Squats':
            st.image(muscle_group_pics[278], width = 200)
        if selected_exercise == 'Walking Lunges':
            st.image(muscle_group_pics[280], width = 200)
        if selected_exercise == 'Step-Ups':
            st.image(muscle_group_pics[282], width = 200)
        if selected_exercise == 'Belt Squat':
            st.image(muscle_group_pics[284], width = 200)
        if selected_exercise == 'Hack Squat':
            st.image(muscle_group_pics[286], width = 200)
        if selected_exercise == 'Front Rack Lunges':
            st.image(muscle_group_pics[288], width = 200)
        if selected_exercise == 'Front Squats':
            st.image(muscle_group_pics[290], width = 200)
        if selected_exercise == 'Back Squats':
            st.image(muscle_group_pics[292], width = 200)
        if selected_exercise == 'Zercher Squats':
            st.image(muscle_group_pics[294], width = 200)
        if selected_exercise == 'Goblet Squats':
            st.image(muscle_group_pics[296], width = 200)
        if selected_exercise == 'Overhead Walking Lunges':
            st.image(muscle_group_pics[298], width = 200)
        if selected_exercise == 'Landmine Squats':
            st.image(muscle_group_pics[200], width = 200)
        if selected_exercise == 'Sled Drag':
            st.image(muscle_group_pics[302], width = 200)
        if selected_exercise == 'Treadmill':
            st.image(muscle_group_pics[304], width = 200)
        if selected_exercise == 'Assault Air Bike':
            st.image(muscle_group_pics[306], width = 200)
        if selected_exercise == 'Elliptical':
            st.image(muscle_group_pics[308], width = 200)
        if selected_exercise == 'Thrusters':
            st.image(muscle_group_pics[310], width = 200)
        if selected_exercise == 'Snatch':
            st.image(muscle_group_pics[312], width = 200)
        if selected_exercise == 'Hang Snatch':
            st.image(muscle_group_pics[314], width = 200)
        if selected_exercise == 'Clean':
            st.image(muscle_group_pics[316], width = 200)
        if selected_exercise == 'Hang Clean':
            st.image(muscle_group_pics[318], width = 200)
        if selected_exercise == 'Power Clean':
            st.image(muscle_group_pics[320], width = 200)
        if selected_exercise == 'Overhead Squat':
            st.image(muscle_group_pics[322], width = 200)
        if selected_exercise == 'Burpees':
            st.image(muscle_group_pics[324], width = 200)
        if selected_exercise == 'Wall Balls':
            st.image(muscle_group_pics[326], width = 200)
        if selected_exercise == 'Leg Extensions':
            st.image(muscle_group_pics[328], width = 200)
        if selected_exercise == 'Sissy Squats':
            st.image(muscle_group_pics[330], width = 200)
        if selected_exercise == 'Wall Sit':
            st.image(muscle_group_pics[332], width = 200)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(muscle_group_pics[334], width = 200)
        if selected_exercise == 'Muscle Snatch':
            st.image(muscle_group_pics[336], width = 200)
        if selected_exercise == "Devil's Press":
            st.image(muscle_group_pics[338], width = 200)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(muscle_group_pics[340], width = 200)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(muscle_group_pics[342], width = 200)
        if selected_exercise == 'Front Raises':
            st.image(muscle_group_pics[344], width = 200)
        if selected_exercise == 'Bottoms-Up Overhead Press':
            st.image(muscle_group_pics[346], width = 200)
        if selected_exercise == 'Bottoms-Up Bench Press':
            st.image(muscle_group_pics[348], width = 200)
        if selected_exercise == 'Bottoms-Up Incline Press':
            st.image(muscle_group_pics[350], width = 200)
        if selected_exercise == 'Single-Arm Snatch':
            st.image(muscle_group_pics[352], width = 200)
        if selected_exercise == 'Power Snatch':
            st.image(muscle_group_pics[354], width = 200)
        if selected_exercise == 'Muscle Clean':
            st.image(muscle_group_pics[356], width = 200)
        if selected_exercise == 'Clean & Press':
            st.image(muscle_group_pics[358], width = 200)
        if selected_exercise == "Waiter's Walk":
            st.image(muscle_group_pics[360], width = 200)
        if selected_exercise == 'Lateral Raises':
            st.image(muscle_group_pics[362], width = 200)
        if selected_exercise == 'Landmine Lateral Raises':
            st.image(muscle_group_pics[364], width = 200)
        if selected_exercise == 'Single-Arm Overhead Press':
            st.image(muscle_group_pics[366], width = 200)
        if selected_exercise == 'Standing Overhead Press':
            st.image(muscle_group_pics[368], width = 200)
        if selected_exercise == 'Seated Overhead Press':
            st.image(muscle_group_pics[370], width = 200)
        if selected_exercise == 'Single-Arm Landmine Press':
            st.image(muscle_group_pics[372], width = 200)
        if selected_exercise == 'Arnold Press':
            st.image(muscle_group_pics[374], width = 200)
        if selected_exercise == 'Z-Press':
            st.image(muscle_group_pics[376], width = 200)
        if selected_exercise == '3-Way Reaches':
            st.image(muscle_group_pics[378], width = 200)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(muscle_group_pics[380], width = 200)
        if selected_exercise == "I-Y-T's":
            st.image(muscle_group_pics[382], width = 200)
        if selected_exercise == 'Standing Horizontal Press':
            st.image(muscle_group_pics[384], width = 200)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(muscle_group_pics[386], width = 200)
        if selected_exercise == 'Turkish Get-Up':
            st.image(muscle_group_pics[388], width = 200)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(muscle_group_pics[390], width = 200)
        if selected_exercise == 'Shoulder Internal Rotations':
            st.image(muscle_group_pics[392], width = 200)
        if selected_exercise == 'Shrugs':
            st.image(muscle_group_pics[394], width = 200)
        if selected_exercise == 'Upright Rows':
            st.image(muscle_group_pics[396], width = 200)
        if selected_exercise == 'Tricep Kickbacks':
            st.image(muscle_group_pics[398], width = 200)
        if selected_exercise == 'Dips':
            st.image(muscle_group_pics[400], width = 200)
        if selected_exercise == 'Dips (Assisted)':
            st.image(muscle_group_pics[402], width = 200)
        if selected_exercise == 'Skull Crushers':
            st.image(muscle_group_pics[404], width = 200)
        if selected_exercise == 'Overhead Tricep Extensions':
            st.image(muscle_group_pics[406], width = 200)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(muscle_group_pics[408], width = 200)
        if selected_exercise == 'Seal Rows':
            st.image(muscle_group_pics[410], width = 200)
        if selected_exercise == 'Seated Rows':
            st.image(muscle_group_pics[412], width = 200)
        if selected_exercise == 'Sled Pulls':
            st.image(muscle_group_pics[414], width = 200)
        if selected_exercise == 'Inverted Row':
            st.image(muscle_group_pics[416], width = 200)
        if selected_exercise == 'Landmine Rows':
            st.image(muscle_group_pics[418], width = 200)
        if selected_exercise == 'Bent Over Rows':
            st.image(muscle_group_pics[420], width = 200)
        if selected_exercise == 'Single-Arm Rows':
            st.image(muscle_group_pics[422], width = 200)
        if selected_exercise == 'Rower':
            st.image(muscle_group_pics[424], width = 200)
        if selected_exercise == 'Face Pulls':
            st.image(muscle_group_pics[426], width = 200)
        if selected_exercise == 'Reverse Flys':
            st.image(muscle_group_pics[428], width = 200)
        if selected_exercise == 'Renegade Rows':
            st.image(muscle_group_pics[430], width = 200)
        if selected_exercise == 'Pull Throughs':
            st.image(muscle_group_pics[432], width = 200)
        if selected_exercise == 'Front Loaded Carry':
            st.image(muscle_group_pics[434], width = 200)
        if selected_exercise == 'Push Press':
            st.image(muscle_group_pics[436], width = 200)

    with col_2:
        if selected_exercise == 'Sit-Ups':
            st.image(muscle_group_pics[1], width = 200)
        if selected_exercise == 'G.H.D. Sit-Ups':
            st.image(muscle_group_pics[3], width = 200)
        if selected_exercise == 'Flutter Kicks':
            st.image(muscle_group_pics[5], width = 200)
        if selected_exercise == 'Lying Leg Raises':
            st.image(muscle_group_pics[7], width = 200)
        if selected_exercise == 'In & Outs':
            st.image(muscle_group_pics[9], width = 200)
        if selected_exercise == 'Scissor Kicks':
            st.image(muscle_group_pics[11], width = 200)
        if selected_exercise == 'Decline Sit-Ups':
            st.image(muscle_group_pics[13], width = 200)
        if selected_exercise == 'Decline Reverse Crunch':
            st.image(muscle_group_pics[15], width = 200)
        if selected_exercise == 'Hanging Knee Raises':
            st.image(muscle_group_pics[17], width = 200)
        if selected_exercise == 'Hanging Leg Raises':
            st.image(muscle_group_pics[19], width = 200)
        if selected_exercise == 'Toes-To-Bar':
            st.image(muscle_group_pics[21], width = 200)
        if selected_exercise == 'Dead Bugs':
            st.image(muscle_group_pics[23], width = 200)
        if selected_exercise == 'Lying Knee Tucks':
            st.image(muscle_group_pics[25], width = 200)
        if selected_exercise == 'Sit-Ups w/ Ball Toss':
            st.image(muscle_group_pics[27], width = 200)
        if selected_exercise == 'Knee Tuck Holds':
            st.image(muscle_group_pics[29], width = 200)
        if selected_exercise == 'Knee Tuck Planks':
            st.image(muscle_group_pics[31], width = 200)
        if selected_exercise == 'Planks':
            st.image(muscle_group_pics[33], width = 200)
        if selected_exercise == 'Side Step Planks':
            st.image(muscle_group_pics[35], width = 200)
        if selected_exercise == 'Lying Leg Circles':
            st.image(muscle_group_pics[37], width = 200)
        if selected_exercise == 'Ab Bicycle':
            st.image(muscle_group_pics[39], width = 200)
        if selected_exercise == 'Banana/Cannon Ball':
            st.image(muscle_group_pics[41], width = 200)
        if selected_exercise == 'Hollow Body Holds':
            st.image(muscle_group_pics[43], width = 200)
        if selected_exercise == 'Ball Slams':
            st.image(muscle_group_pics[45], width = 200)
        if selected_exercise == 'Stir-The-Pot':
            st.image(muscle_group_pics[47], width = 200)
        if selected_exercise == 'Sledgehammer Strikes':
            st.image(muscle_group_pics[49], width = 200)
        if selected_exercise == 'Roll-Outs':
            st.image(muscle_group_pics[51], width = 200)
        if selected_exercise == 'Kneeling Crunches':
            st.image(muscle_group_pics[53], width = 200)
        if selected_exercise == 'Lateral Band Walks':
            st.image(muscle_group_pics[55], width = 200)
        if selected_exercise == 'Standing Hip Abductions':
            st.image(muscle_group_pics[57], width = 200)
        if selected_exercise == 'Seated Hip Abductions':
            st.image(muscle_group_pics[59], width = 200)
        if selected_exercise == 'Side Lying Hip Abductions':
            st.image(muscle_group_pics[61], width = 200)
        if selected_exercise == 'Side Plank Clamshells':
            st.image(muscle_group_pics[63], width = 200)
        if selected_exercise == 'Copenhagen Plank':
            st.image(muscle_group_pics[65], width = 200)
        if selected_exercise == 'Seated Hip Adductions':
            st.image(muscle_group_pics[67], width = 200)
        if selected_exercise == 'Standing Hip Adductions':
            st.image(muscle_group_pics[69], width = 200)
        if selected_exercise == 'Adductor Leg Lifts':
            st.image(muscle_group_pics[71], width = 200)
        if selected_exercise == 'Shin Curls':
            st.image(muscle_group_pics[73], width = 200)
        if selected_exercise == 'Heel Walks':
            st.image(muscle_group_pics[75], width = 200)
        if selected_exercise == 'Hammer Curls':
            st.image(muscle_group_pics[77], width = 200)
        if selected_exercise == 'Seated Incline Bicep Curl':
            st.image(muscle_group_pics[79], width = 200)
        if selected_exercise == 'Bicep Curl':
            st.image(muscle_group_pics[81], width = 200)
        if selected_exercise == 'Preacher Curl':
            st.image(muscle_group_pics[83], width = 200)
        if selected_exercise == 'Rope Climbs':
            st.image(muscle_group_pics[85], width = 200)
        if selected_exercise == 'Jumping Rope':
            st.image(muscle_group_pics[87], width = 200)
        if selected_exercise == 'Calf Raises':
            st.image(muscle_group_pics[89], width = 200)
        if selected_exercise == 'Seated Calf Raises':
            st.image(muscle_group_pics[91], width = 200)
        if selected_exercise == 'Single-Leg Calf Raises':
            st.image(muscle_group_pics[93], width = 200)
        if selected_exercise == 'Chest Flys':
            st.image(muscle_group_pics[95], width = 200)
        if selected_exercise == 'Incline Chest Flys':
            st.image(muscle_group_pics[97], width = 200)
        if selected_exercise == 'Decline Chest Flys':
            st.image(muscle_group_pics[99], width = 200)
        if selected_exercise == 'Push-Ups':
            st.image(muscle_group_pics[101], width = 200)
        if selected_exercise == 'Bench Press':
            st.image(muscle_group_pics[103], width = 200)
        if selected_exercise == 'Incline Bench Press':
            st.image(muscle_group_pics[105], width = 200)
        if selected_exercise == 'Decline Bench Press':
            st.image(muscle_group_pics[107], width = 200)
        if selected_exercise == 'Squeeze Press':
            st.image(muscle_group_pics[109], width = 200)
        if selected_exercise == 'Floor Press':
            st.image(muscle_group_pics[111], width = 200)
        if selected_exercise == 'Kneeling Chest Pass':
            st.image(muscle_group_pics[113], width = 200)
        if selected_exercise == "Farmer's Walk":
            st.image(muscle_group_pics[115], width = 200)
        if selected_exercise == 'Wrist Roller':
            st.image(muscle_group_pics[117], width = 200)
        if selected_exercise == 'Standing Hip Extensions':
            st.image(muscle_group_pics[119], width = 200)
        if selected_exercise == 'Donkey Kicks':
            st.image(muscle_group_pics[121], width = 200)
        if selected_exercise == 'Hip Thrusters':
            st.image(muscle_group_pics[123], width = 200)
        if selected_exercise == 'Glute Drive Machine':
            st.image(muscle_group_pics[125], width = 200)
        if selected_exercise == 'Glute Bridges':
            st.image(muscle_group_pics[127], width = 200)
        if selected_exercise == 'Single-Leg Hip Thrusters':
            st.image(muscle_group_pics[129], width = 200)
        if selected_exercise == 'Single-Leg Glute Bridge':
            st.image(muscle_group_pics[131], width = 200)
        if selected_exercise == 'Single-Leg Pull Throughs':
            st.image(muscle_group_pics[133], width = 200)
        if selected_exercise == 'Shin Hops':
            st.image(muscle_group_pics[135], width = 200)
        if selected_exercise == 'Glute Ham Raises':
            st.image(muscle_group_pics[137], width = 200)
        if selected_exercise == 'Standing Leg Curls':
            st.image(muscle_group_pics[139], width = 200)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(muscle_group_pics[141], width = 200)
        if selected_exercise == 'Kettlebell Swings':
            st.image(muscle_group_pics[143], width = 200)
        if selected_exercise == 'Romanian Deadlift':
            st.image(muscle_group_pics[145], width = 200)
        if selected_exercise == 'Single-Leg Romanian Deadlift':
            st.image(muscle_group_pics[147], width = 200)
        if selected_exercise == 'Good Mornings':
            st.image(muscle_group_pics[149], width = 200)
        if selected_exercise == 'Air Runner (Self-Powered Treadmill)':
            st.image(muscle_group_pics[151], width = 200)
        if selected_exercise == 'Snatch High Pull':
            st.image(muscle_group_pics[153], width = 200)
        if selected_exercise == 'Clean High Pull':
            st.image(muscle_group_pics[155], width = 200)
        if selected_exercise == 'Snatch Pull':
            st.image(muscle_group_pics[157], width = 200)
        if selected_exercise == 'Clean Pull':
            st.image(muscle_group_pics[159], width = 200)
        if selected_exercise == 'Lying Leg Curls (Floor)':
            st.image(muscle_group_pics[161], width = 200)
        if selected_exercise == 'Lying Leg Curls (Machine)':
            st.image(muscle_group_pics[163], width = 200)
        if selected_exercise == 'Banded Marches':
            st.image(muscle_group_pics[165], width = 200)
        if selected_exercise == 'Chin-Ups':
            st.image(muscle_group_pics[167], width = 200)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(muscle_group_pics[169], width = 200)
        if selected_exercise == 'Pull-Ups':
            st.image(muscle_group_pics[171], width = 200)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(muscle_group_pics[173], width = 200)
        if selected_exercise == 'Lat Pulldown':
            st.image(muscle_group_pics[175], width = 200)
        if selected_exercise == 'Neutral-Grip Lat Pulldown':
            st.image(muscle_group_pics[177], width = 200)
        if selected_exercise == 'Single-Arm Lat Pulldown':
            st.image(muscle_group_pics[179], width = 200)
        if selected_exercise == 'Chin-Up Grip Lat Pulldown':
            st.image(muscle_group_pics[181], width = 200)
        if selected_exercise == 'Pull-Overs':
            st.image(muscle_group_pics[183], width = 200)
        if selected_exercise == 'Ski Erg':
            st.image(muscle_group_pics[185], width = 200)
        if selected_exercise == 'Straight-Arm Lat Pulldown':
            st.image(muscle_group_pics[187], width = 200)
        if selected_exercise == 'Back Extensions':
            st.image(muscle_group_pics[189], width = 200)
        if selected_exercise == 'Reverse Hypers':
            st.image(muscle_group_pics[191], width = 200)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(muscle_group_pics[193], width = 200)
        if selected_exercise == 'Bird Dog':
            st.image(muscle_group_pics[195], width = 200)
        if selected_exercise == 'Deadlift':
            st.image(muscle_group_pics[197], width = 200)
        if selected_exercise == 'Supermans':
            st.image(muscle_group_pics[199], width = 200)
        if selected_exercise == 'Lying Heel Touches':
            st.image(muscle_group_pics[201], width = 200)
        if selected_exercise == 'Windshield Wipers':
            st.image(muscle_group_pics[203], width = 200)
        if selected_exercise == 'Hanging Oblique Knee Raises':
            st.image(muscle_group_pics[205], width = 200)
        if selected_exercise == 'Pallof Press Holds':
            st.image(muscle_group_pics[207], width = 200)
        if selected_exercise == 'Pallof Press':
            st.image(muscle_group_pics[209], width = 200)
        if selected_exercise == 'Russian Twists':
            st.image(muscle_group_pics[211], width = 200)
        if selected_exercise == 'Hanging Windshield Wipers':
            st.image(muscle_group_pics[213], width = 200)
        if selected_exercise == 'Around-The-Worlds':
            st.image(muscle_group_pics[215], width = 200)
        if selected_exercise == 'Side Bends':
            st.image(muscle_group_pics[217], width = 200)
        if selected_exercise == "Single-Arm Farmer's Walk":
            st.image(muscle_group_pics[219], width = 200)
        if selected_exercise == 'Side Planks':
            st.image(muscle_group_pics[221], width = 200)
        if selected_exercise == 'Side Plank Pulses':
            st.image(muscle_group_pics[223], width = 200)
        if selected_exercise == 'Lateral Ball Throws':
            st.image(muscle_group_pics[225], width = 200)
        if selected_exercise == 'Lateral Ball Slams':
            st.image(muscle_group_pics[227], width = 200)
        if selected_exercise == 'Standing High-To-Low Twist':
            st.image(muscle_group_pics[229], width = 200)
        if selected_exercise == 'Shoulder Taps':
            st.image(muscle_group_pics[231], width = 200)
        if selected_exercise == 'Contact Twists':
            st.image(muscle_group_pics[233], width = 200)
        if selected_exercise == 'Box Jumps':
            st.image(muscle_group_pics[235], width = 200)
        if selected_exercise == 'Depth Jumps':
            st.image(muscle_group_pics[237], width = 200)
        if selected_exercise == 'Depth Drops':
            st.image(muscle_group_pics[239], width = 200)
        if selected_exercise == 'Hurdle Jumps':
            st.image(muscle_group_pics[241], width = 200)
        if selected_exercise == 'Broad Jumps':
            st.image(muscle_group_pics[243], width = 200)
        if selected_exercise == 'Explosive Step-Ups':
            st.image(muscle_group_pics[245], width = 200)
        if selected_exercise == 'Lateral Hurdle Jumps':
            st.image(muscle_group_pics[247], width = 200)
        if selected_exercise == 'Bike Erg':
            st.image(muscle_group_pics[249], width = 200)
        if selected_exercise == 'Stairmaster':
            st.image(muscle_group_pics[251], width = 200)
        if selected_exercise == 'Speed Skater Jumps':
            st.image(muscle_group_pics[253], width = 200)
        if selected_exercise == 'Sled Push':
            st.image(muscle_group_pics[255], width = 200)
        if selected_exercise == 'Plyo Lunges':
            st.image(muscle_group_pics[257], width = 200)
        if selected_exercise == 'Reverse Sled Drag':
            st.image(muscle_group_pics[259], width = 200)
        if selected_exercise == 'Lateral Lunges':
            st.image(muscle_group_pics[261], width = 200)
        if selected_exercise == 'Lateral Sled Drag':
            st.image(muscle_group_pics[263], width = 200)
        if selected_exercise == 'Leg Press':
            st.image(muscle_group_pics[265], width = 200)
        if selected_exercise == 'Single-Leg Leg Press':
            st.image(muscle_group_pics[267], width = 200)
        if selected_exercise == 'Reverse Lunges':
            st.image(muscle_group_pics[269], width = 200)
        if selected_exercise == 'Box Squats':
            st.image(muscle_group_pics[271], width = 200)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(muscle_group_pics[273], width = 200)
        if selected_exercise == 'Foot Elevated Reverse Lunges':
            st.image(muscle_group_pics[275], width = 200)
        if selected_exercise == 'Single-Leg Box Squats':
            st.image(muscle_group_pics[277], width = 200)
        if selected_exercise == 'Pistol Squats':
            st.image(muscle_group_pics[279], width = 200)
        if selected_exercise == 'Walking Lunges':
            st.image(muscle_group_pics[281], width = 200)
        if selected_exercise == 'Step-Ups':
            st.image(muscle_group_pics[283], width = 200)
        if selected_exercise == 'Belt Squat':
            st.image(muscle_group_pics[285], width = 200)
        if selected_exercise == 'Hack Squat':
            st.image(muscle_group_pics[287], width = 200)
        if selected_exercise == 'Front Rack Lunges':
            st.image(muscle_group_pics[289], width = 200)
        if selected_exercise == 'Front Squats':
            st.image(muscle_group_pics[291], width = 200)
        if selected_exercise == 'Back Squats':
            st.image(muscle_group_pics[293], width = 200)
        if selected_exercise == 'Zercher Squats':
            st.image(muscle_group_pics[295], width = 200)
        if selected_exercise == 'Goblet Squats':
            st.image(muscle_group_pics[297], width = 200)
        if selected_exercise == 'Overhead Walking Lunges':
            st.image(muscle_group_pics[299], width = 200)
        if selected_exercise == 'Landmine Squats':
            st.image(muscle_group_pics[301], width = 200)
        if selected_exercise == 'Sled Drag':
            st.image(muscle_group_pics[303], width = 200)
        if selected_exercise == 'Treadmill':
            st.image(muscle_group_pics[305], width = 200)
        if selected_exercise == 'Assault Air Bike':
            st.image(muscle_group_pics[307], width = 200)
        if selected_exercise == 'Elliptical':
            st.image(muscle_group_pics[309], width = 200)
        if selected_exercise == 'Thrusters':
            st.image(muscle_group_pics[311], width = 200)
        if selected_exercise == 'Snatch':
            st.image(muscle_group_pics[313], width = 200)
        if selected_exercise == 'Hang Snatch':
            st.image(muscle_group_pics[315], width = 200)
        if selected_exercise == 'Clean':
            st.image(muscle_group_pics[317], width = 200)
        if selected_exercise == 'Hang Clean':
            st.image(muscle_group_pics[319], width = 200)
        if selected_exercise == 'Power Clean':
            st.image(muscle_group_pics[321], width = 200)
        if selected_exercise == 'Overhead Squat':
            st.image(muscle_group_pics[323], width = 200)
        if selected_exercise == 'Burpees':
            st.image(muscle_group_pics[325], width = 200)
        if selected_exercise == 'Wall Balls':
            st.image(muscle_group_pics[327], width = 200)
        if selected_exercise == 'Leg Extensions':
            st.image(muscle_group_pics[329], width = 200)
        if selected_exercise == 'Sissy Squats':
            st.image(muscle_group_pics[331], width = 200)
        if selected_exercise == 'Wall Sit':
            st.image(muscle_group_pics[333], width = 200)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(muscle_group_pics[335], width = 200)
        if selected_exercise == 'Muscle Snatch':
            st.image(muscle_group_pics[337], width = 200)
        if selected_exercise == "Devil's Press":
            st.image(muscle_group_pics[339], width = 200)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(muscle_group_pics[341], width = 200)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(muscle_group_pics[343], width = 200)
        if selected_exercise == 'Front Raises':
            st.image(muscle_group_pics[345], width = 200)
        if selected_exercise == 'Bottoms-Up Overhead Press':
            st.image(muscle_group_pics[347], width = 200)
        if selected_exercise == 'Bottoms-Up Bench Press':
            st.image(muscle_group_pics[349], width = 200)
        if selected_exercise == 'Bottoms-Up Incline Press':
            st.image(muscle_group_pics[351], width = 200)
        if selected_exercise == 'Single-Arm Snatch':
            st.image(muscle_group_pics[353], width = 200)
        if selected_exercise == 'Power Snatch':
            st.image(muscle_group_pics[355], width = 200)
        if selected_exercise == 'Muscle Clean':
            st.image(muscle_group_pics[357], width = 200)
        if selected_exercise == 'Clean & Press':
            st.image(muscle_group_pics[359], width = 200)
        if selected_exercise == "Waiter's Walk":
            st.image(muscle_group_pics[361], width = 200)
        if selected_exercise == 'Lateral Raises':
            st.image(muscle_group_pics[363], width = 200)
        if selected_exercise == 'Landmine Lateral Raises':
            st.image(muscle_group_pics[365], width = 200)
        if selected_exercise == 'Single-Arm Overhead Press':
            st.image(muscle_group_pics[367], width = 200)
        if selected_exercise == 'Standing Overhead Press':
            st.image(muscle_group_pics[369], width = 200)
        if selected_exercise == 'Seated Overhead Press':
            st.image(muscle_group_pics[371], width = 200)
        if selected_exercise == 'Single-Arm Landmine Press':
            st.image(muscle_group_pics[373], width = 200)
        if selected_exercise == 'Arnold Press':
            st.image(muscle_group_pics[375], width = 200)
        if selected_exercise == 'Z-Press':
            st.image(muscle_group_pics[377], width = 200)
        if selected_exercise == '3-Way Reaches':
            st.image(muscle_group_pics[379], width = 200)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(muscle_group_pics[381], width = 200)
        if selected_exercise == "I-Y-T's":
            st.image(muscle_group_pics[383], width = 200)
        if selected_exercise == 'Standing Horizontal Press':
            st.image(muscle_group_pics[385], width = 200)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(muscle_group_pics[387], width = 200)
        if selected_exercise == 'Turkish Get-Up':
            st.image(muscle_group_pics[389], width = 200)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(muscle_group_pics[391], width = 200)
        if selected_exercise == 'Shoulder Internal Rotations':
            st.image(muscle_group_pics[393], width = 200)
        if selected_exercise == 'Shrugs':
            st.image(muscle_group_pics[395], width = 200)
        if selected_exercise == 'Upright Rows':
            st.image(muscle_group_pics[397], width = 200)
        if selected_exercise == 'Tricep Kickbacks':
            st.image(muscle_group_pics[399], width = 200)
        if selected_exercise == 'Dips':
            st.image(muscle_group_pics[401], width = 200)
        if selected_exercise == 'Dips (Assisted)':
            st.image(muscle_group_pics[403], width = 200)
        if selected_exercise == 'Skull Crushers':
            st.image(muscle_group_pics[405], width = 200)
        if selected_exercise == 'Overhead Tricep Extensions':
            st.image(muscle_group_pics[407], width = 200)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(muscle_group_pics[409], width = 200)
        if selected_exercise == 'Seal Rows':
            st.image(muscle_group_pics[411], width = 200)
        if selected_exercise == 'Seated Rows':
            st.image(muscle_group_pics[413], width = 200)
        if selected_exercise == 'Sled Pulls':
            st.image(muscle_group_pics[415], width = 200)
        if selected_exercise == 'Inverted Row':
            st.image(muscle_group_pics[417], width = 200)
        if selected_exercise == 'Landmine Rows':
            st.image(muscle_group_pics[419], width = 200)
        if selected_exercise == 'Bent Over Rows':
            st.image(muscle_group_pics[421], width = 200)
        if selected_exercise == 'Single-Arm Rows':
            st.image(muscle_group_pics[423], width = 200)
        if selected_exercise == 'Rower':
            st.image(muscle_group_pics[425], width = 200)
        if selected_exercise == 'Face Pulls':
            st.image(muscle_group_pics[427], width = 200)
        if selected_exercise == 'Reverse Flys':
            st.image(muscle_group_pics[429], width = 200)
        if selected_exercise == 'Renegade Rows':
            st.image(muscle_group_pics[431], width = 200)
        if selected_exercise == 'Pull Throughs':
            st.image(muscle_group_pics[433], width = 200)
        if selected_exercise == 'Front Loaded Carry':
            st.image(muscle_group_pics[435], width = 200)
        if selected_exercise == 'Push Press':
            st.image(muscle_group_pics[437], width = 200)

    with col_3:
        if selected_exercise != '':
            desc_1 = df[df["Name"] == selected_exercise]["Difficulty Level"].values[0]
            st.markdown(f'**Difficulty Level:** {desc_1} out of 5')
            desc_2 = df[df["Name"] == selected_exercise]["Category"].values[0]
            st.markdown(f'**Category:** {desc_2}')
            desc_3 = df[df["Name"] == selected_exercise]["Equipment Options"].values[0]
            st.markdown(f'**Equipment Options:** {desc_3}')
            desc_4 = df[df["Name"] == selected_exercise]["Primary Muscle Group"].values[0]
            st.markdown(f'**Primary Muscle Group:** {desc_4}')
            desc_5 = df[df["Name"] == selected_exercise]["Secondary Muscle Group(s)"].values[0]
            st.markdown(f'**Secondary Muscle Group(s):** {desc_5}')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    st.header('Example Picture(s)')
    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        if selected_exercise == '3-Way Reaches':
            st.image(demo_pics[0], width = 300)
        if selected_exercise == 'Ab Bicycle':
            st.image(demo_pics[3], width = 300)
        if selected_exercise == 'Adductor Leg Lifts':
            st.image(demo_pics[5], width = 300)
        if selected_exercise == 'Air Runner (Self-Powered Treadmill)':
            st.image(demo_pics[6], width = 300)
        if selected_exercise == 'Arnold Press':
            st.image(demo_pics[8], width = 300)
        if selected_exercise == 'Around-The-Worlds':
            st.image(demo_pics[10], width = 300)
        if selected_exercise == 'Assault Air Bike':
            st.image(demo_pics[14], width = 300)
        if selected_exercise == 'Back Extensions':
            st.image(demo_pics[16], width = 300)
        if selected_exercise == 'Back Squats':
            st.image(demo_pics[18], width = 300)
        if selected_exercise == 'Banana/Cannon Ball':
            st.image(demo_pics[20], width = 300)
        if selected_exercise == 'Banded Marches':
            st.image(demo_pics[24], width = 300)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[31], width = 300)
        if selected_exercise == 'Belt Squat':
            st.image(demo_pics[41], width = 300)
        if selected_exercise == 'Bench Press':
            st.image(demo_pics[44], width = 300)
        if selected_exercise == 'Bent Over Rows':
            st.image(demo_pics[47], width = 300)
        if selected_exercise == 'Bicep Curl':
            st.image(demo_pics[50], width = 300)
        if selected_exercise == 'Bike Erg':
            st.image(demo_pics[56], width = 300)
        if selected_exercise == 'Bird Dog':
            st.image(demo_pics[57], width = 300)
        if selected_exercise == 'Bottoms-Up Bench Press':
            st.image(demo_pics[59], width = 300)
        if selected_exercise == 'Bottoms-Up Incline Press':
            st.image(demo_pics[61], width = 300)
        if selected_exercise == 'Bottoms-Up Overhead Press':
            st.image(demo_pics[63], width = 300)
        if selected_exercise == 'Box Jumps':
            st.image(demo_pics[65], width = 300)
        if selected_exercise == 'Box Squats':
            st.image(demo_pics[69], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[72], width = 300)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(demo_pics[80], width = 300)
        if selected_exercise == 'Burpees':
            st.image(demo_pics[85], width = 300)
        if selected_exercise == 'Calf Raises':
            st.image(demo_pics[86], width = 300)
        if selected_exercise == 'Chest Flys':
            st.image(demo_pics[90], width = 300)
        if selected_exercise == 'Chin-Up Grip Lat Pulldown':
            st.image(demo_pics[96], width = 300)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(demo_pics[98], width = 300)
        if selected_exercise == 'Chin-Ups':
            st.image(demo_pics[104], width = 300)
        if selected_exercise == 'Clean & Press':
            st.image(demo_pics[106], width = 300)
        if selected_exercise == 'Clean High Pull':
            st.image(demo_pics[112], width = 300)
        if selected_exercise == 'Clean Pull':
            st.image(demo_pics[117], width = 300)
        if selected_exercise == 'Clean':
            st.image(demo_pics[121], width = 300)
        if selected_exercise == 'Contact Twists':
            st.image(demo_pics[122], width = 300)
        if selected_exercise == 'Copenhagen Plank':
            st.image(demo_pics[124], width = 300)
        if selected_exercise == 'Dead Bugs':
            st.image(demo_pics[127], width = 300)
        if selected_exercise == 'Deadlift':
            st.image(demo_pics[130], width = 300)
        if selected_exercise == 'Decline Bench Press':
            st.image(demo_pics[136], width = 300)
        if selected_exercise == 'Decline Chest Flys':
            st.image(demo_pics[140], width = 300)
        if selected_exercise == 'Decline Reverse Crunch':
            st.image(demo_pics[146], width = 300)
        if selected_exercise == 'Decline Sit-Ups':
            st.image(demo_pics[148], width = 300)
        if selected_exercise == 'Depth Drops':
            st.image(demo_pics[150], width = 300)
        if selected_exercise == 'Depth Jumps':
            st.image(demo_pics[154], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[156], width = 300)
        if selected_exercise == 'Dips (Assisted)':
            st.image(demo_pics[163], width = 300)
        if selected_exercise == 'Dips':
            st.image(demo_pics[169], width = 300)
        if selected_exercise == 'Donkey Kicks':
            st.image(demo_pics[172], width = 300)
        if selected_exercise == 'Ball Slams':
            st.image(demo_pics[175], width = 300)
        if selected_exercise == 'Elliptical':
            st.image(demo_pics[176], width = 300)
        if selected_exercise == 'Explosive Step-Ups':
            st.image(demo_pics[178], width = 300)
        if selected_exercise == 'Face Pulls':
            st.image(demo_pics[179], width = 300)
        if selected_exercise == "Farmer's Walk":
            st.image(demo_pics[183], width = 300)
        if selected_exercise == 'Floor Press':
            st.image(demo_pics[186], width = 300)
        if selected_exercise == 'Flutter Kicks':
            st.image(demo_pics[192], width = 300)
        if selected_exercise == 'Foot Elevated Reverse Lunges':
            st.image(demo_pics[194], width = 300)
        if selected_exercise == 'Front Rack Lunges':
            st.image(demo_pics[198], width = 300)
        if selected_exercise == 'Front Raises':
            st.image(demo_pics[201], width = 300)
        if selected_exercise == 'Front Squats':
            st.image(demo_pics[205], width = 300)
        if selected_exercise == 'G.H.D. Sit-Ups':
            st.image(demo_pics[208], width = 300)
        if selected_exercise == 'Glute Bridges':
            st.image(demo_pics[209], width = 300)
        if selected_exercise == 'Glute Drive Machine':
            st.image(demo_pics[214], width = 300)
        if selected_exercise == 'Glute Ham Raises':
            st.image(demo_pics[215], width = 300)
        if selected_exercise == 'Goblet Squats':
            st.image(demo_pics[217], width = 300)
        if selected_exercise == 'Good Mornings':
            st.image(demo_pics[223], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[229], width = 300)
        if selected_exercise == 'Hack Squat':
            st.image(demo_pics[241], width = 300)
        if selected_exercise == 'Hammer Curls':
            st.image(demo_pics[244], width = 300)
        if selected_exercise == 'Hang Clean':
            st.image(demo_pics[247], width = 300)
        if selected_exercise == 'Hang Snatch':
            st.image(demo_pics[248], width = 300)
        if selected_exercise == 'Hanging Knee Raises':
            st.image(demo_pics[249], width = 300)
        if selected_exercise == 'Hanging Leg Raises':
            st.image(demo_pics[251], width = 300)
        if selected_exercise == 'Hanging Oblique Knee Raises':
            st.image(demo_pics[253], width = 300)
        if selected_exercise == 'Hanging Windshield Wipers':
            st.image(demo_pics[256], width = 300)
        if selected_exercise == 'Heel Walks':
            st.image(demo_pics[259], width = 300)
        if selected_exercise == 'Hip Thrusters':
            st.image(demo_pics[261], width = 300)
        if selected_exercise == 'Hollow Body Holds':
            st.image(demo_pics[266], width = 300)
        if selected_exercise == 'Hurdle Jumps':
            st.image(demo_pics[267], width = 300)
        if selected_exercise == 'In & Outs':
            st.image(demo_pics[273], width = 300)
        if selected_exercise == 'Incline Bench Press':
            st.image(demo_pics[275], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[279], width = 300)
        if selected_exercise == 'Inverted Row':
            st.image(demo_pics[286], width = 300)
        if selected_exercise == "I-Y-T's":
            st.image(demo_pics[289], width = 300)
        if selected_exercise == 'Jumping Rope':
            st.image(demo_pics[293], width = 300)
        if selected_exercise == 'Kettlebell Swings':
            st.image(demo_pics[295], width = 300)
        if selected_exercise == 'Knee Tuck Holds':
            st.image(demo_pics[297], width = 300)
        if selected_exercise == 'Knee Tuck Planks':
            st.image(demo_pics[299], width = 300)
        if selected_exercise == 'Kneeling Chest Pass':
            st.image(demo_pics[301], width = 300)
        if selected_exercise == 'Kneeling Crunches':
            st.image(demo_pics[303], width = 300)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(demo_pics[305], width = 300)
        if selected_exercise == 'Landmine Lateral Raises':
            st.image(demo_pics[312], width = 300)
        if selected_exercise == 'Landmine Rows':
            st.image(demo_pics[316], width = 300)
        if selected_exercise == 'Landmine Squats':
            st.image(demo_pics[318], width = 300)
        if selected_exercise == 'Lat Pulldown':
            st.image(demo_pics[321], width = 300)
        if selected_exercise == 'Lateral Ball Slams':
            st.image(demo_pics[322], width = 300)
        if selected_exercise == 'Lateral Ball Throws':
            st.image(demo_pics[323], width = 300)
        if selected_exercise == 'Lateral Band Walks':
            st.image(demo_pics[325], width = 300)
        if selected_exercise == 'Lateral Hurdle Jumps':
            st.image(demo_pics[327], width = 300)
        if selected_exercise == 'Lateral Lunges':
            st.image(demo_pics[330], width = 300)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(demo_pics[334], width = 300)
        if selected_exercise == 'Lateral Raises':
            st.image(demo_pics[340], width = 300)
        if selected_exercise == 'Lateral Sled Drag':
            st.image(demo_pics[343], width = 300)
        if selected_exercise == 'Leg Extensions':
            st.image(demo_pics[346], width = 300)
        if selected_exercise == 'Leg Press':
            st.image(demo_pics[350], width = 300)
        if selected_exercise == 'Lying Heel Touches':
            st.image(demo_pics[352], width = 300)
        if selected_exercise == 'Lying Leg Circles':
            st.image(demo_pics[354], width = 300)
        if selected_exercise == 'Lying Knee Tucks':
            st.image(demo_pics[356], width = 300)
        if selected_exercise == 'Lying Leg Curls (Floor)':
            st.image(demo_pics[359], width = 300)
        if selected_exercise == 'Lying Leg Curls (Machine)':
            st.image(demo_pics[362], width = 300)
        if selected_exercise == 'Lying Leg Raises':
            st.image(demo_pics[365], width = 300)
        if selected_exercise == 'Muscle Clean':
            st.image(demo_pics[367], width = 300)
        if selected_exercise == 'Muscle Snatch':
            st.image(demo_pics[371], width = 300)
        if selected_exercise == 'Neutral-Grip Lat Pulldown':
            st.image(demo_pics[372], width = 300)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(demo_pics[374], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[379], width = 300)
        if selected_exercise == 'Overhead Squat':
            st.image(demo_pics[387], width = 300)
        if selected_exercise == 'Overhead Tricep Extensions':
            st.image(demo_pics[389], width = 300)
        if selected_exercise == 'Overhead Walking Lunges':
            st.image(demo_pics[393], width = 300)
        if selected_exercise == 'Pallof Press':
            st.image(demo_pics[397], width = 300)
        if selected_exercise == 'Pallof Press Holds':
            st.image(demo_pics[400], width = 300)
        if selected_exercise == 'Pistol Squats':
            st.image(demo_pics[402], width = 300)
        if selected_exercise == 'Planks':
            st.image(demo_pics[408], width = 300)
        if selected_exercise == 'Plyo Lunges':
            st.image(demo_pics[411], width = 300)
        if selected_exercise == 'Power Clean':
            st.image(demo_pics[413], width = 300)
        if selected_exercise == 'Power Snatch':
            st.image(demo_pics[414], width = 300)
        if selected_exercise == 'Preacher Curl':
            st.image(demo_pics[415], width = 300)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(demo_pics[420], width = 300)
        if selected_exercise == 'Pull Throughs':
            st.image(demo_pics[426], width = 300)
        if selected_exercise == 'Pull-Overs':
            st.image(demo_pics[428], width = 300)
        if selected_exercise == 'Pull-Ups':
            st.image(demo_pics[431], width = 300)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(demo_pics[432], width = 300)
        if selected_exercise == 'Push-Ups':
            st.image(demo_pics[437], width = 300)
        if selected_exercise == 'Renegade Rows':
            st.image(demo_pics[443], width = 300)
        if selected_exercise == 'Reverse Flys':
            st.image(demo_pics[445], width = 300)
        if selected_exercise == 'Reverse Hypers':
            st.image(demo_pics[450], width = 300)
        if selected_exercise == 'Reverse Lunges':
            st.image(demo_pics[452], width = 300)
        if selected_exercise == 'Reverse Sled Drag':
            st.image(demo_pics[456], width = 300)
        if selected_exercise == 'Roll-Outs':
            st.image(demo_pics[458], width = 300)
        if selected_exercise == 'Romanian Deadlift':
            st.image(demo_pics[462], width = 300)
        if selected_exercise == 'Rope Climbs':
            st.image(demo_pics[468], width = 300)
        if selected_exercise == 'Rower':
            st.image(demo_pics[471], width = 300)
        if selected_exercise == 'Russian Twists':
            st.image(demo_pics[473], width = 300)
        if selected_exercise == 'Scissor Kicks':
            st.image(demo_pics[476], width = 300)
        if selected_exercise == 'Seal Rows':
            st.image(demo_pics[478], width = 300)
        if selected_exercise == 'Seated Calf Raises':
            st.image(demo_pics[483], width = 300)
        if selected_exercise == 'Seated Hip Abductions':
            st.image(demo_pics[488], width = 300)
        if selected_exercise == 'Seated Hip Adductions':
            st.image(demo_pics[491], width = 300)
        if selected_exercise == 'Seated Incline Bicep Curl':
            st.image(demo_pics[494], width = 300)
        if selected_exercise == 'Seated Overhead Press':
            st.image(demo_pics[495], width = 300)
        if selected_exercise == 'Seated Rows':
            st.image(demo_pics[499], width = 300)
        if selected_exercise == 'Shin Curls':
            st.image(demo_pics[505], width = 300)
        if selected_exercise == 'Shin Hops':
            st.image(demo_pics[509], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[513], width = 300)
        if selected_exercise == 'Shoulder Internal Rotations':
            st.image(demo_pics[520], width = 300)
        if selected_exercise == 'Shoulder Taps':
            st.image(demo_pics[524], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[526], width = 300)
        if selected_exercise == 'Side Bends':
            st.image(demo_pics[534], width = 300)
        if selected_exercise == 'Side Lying Hip Abductions':
            st.image(demo_pics[539], width = 300)
        if selected_exercise == 'Side Plank Clamshells':
            st.image(demo_pics[543], width = 300)
        if selected_exercise == 'Side Plank Pulses':
            st.image(demo_pics[546], width = 300)
        if selected_exercise == 'Side Planks':
            st.image(demo_pics[549], width = 300)
        if selected_exercise == 'Side Step Planks':
            st.image(demo_pics[551], width = 300)
        if selected_exercise == "Single-Arm Farmer's Walk":
            st.image(demo_pics[553], width = 300)
        if selected_exercise == 'Single-Arm Landmine Press':
            st.image(demo_pics[555], width = 300)
        if selected_exercise == 'Single-Arm Lat Pulldown':
            st.image(demo_pics[559], width = 300)
        if selected_exercise == 'Single-Arm Overhead Press':
            st.image(demo_pics[563], width = 300)
        if selected_exercise == 'Single-Arm Rows':
            st.image(demo_pics[567], width = 300)
        if selected_exercise == 'Single-Arm Snatch':
            st.image(demo_pics[573], width = 300)
        if selected_exercise == 'Single-Leg Box Squats':
            st.image(demo_pics[575], width = 300)
        if selected_exercise == 'Single-Leg Calf Raises':
            st.image(demo_pics[579], width = 300)
        if selected_exercise == 'Single-Leg Glute Bridge':
            st.image(demo_pics[581], width = 300)
        if selected_exercise == 'Single-Leg Hip Thrusters':
            st.image(demo_pics[585], width = 300)
        if selected_exercise == 'Single-Leg Leg Press':
            st.image(demo_pics[588], width = 300)
        if selected_exercise == 'Single-Leg Romanian Deadlift':
            st.image(demo_pics[590], width = 300)
        if selected_exercise == 'Sissy Squats':
            st.image(demo_pics[594], width = 300)
        if selected_exercise == 'Sit-Ups':
            st.image(demo_pics[600], width = 300)
        if selected_exercise == 'Ski Erg':
            st.image(demo_pics[602], width = 300)
        if selected_exercise == 'Skull Crushers':
            st.image(demo_pics[603], width = 300)
        if selected_exercise == 'Sled Drag':
            st.image(demo_pics[608], width = 300)
        if selected_exercise == 'Sled Pulls':
            st.image(demo_pics[611], width = 300)
        if selected_exercise == 'Sled Push':
            st.image(demo_pics[613], width = 300)
        if selected_exercise == 'Sledgehammer Strikes':
            st.image(demo_pics[615], width = 300)
        if selected_exercise == 'Snatch':
            st.image(demo_pics[618], width = 300)
        if selected_exercise == 'Snatch High Pull':
            st.image(demo_pics[620], width = 300)
        if selected_exercise == 'Snatch Pull':
            st.image(demo_pics[625], width = 300)
        if selected_exercise == 'Speed Skater Jumps':
            st.image(demo_pics[629], width = 300)
        if selected_exercise == 'Squeeze Press':
            st.image(demo_pics[631], width = 300)
        if selected_exercise == 'Stairmaster':
            st.image(demo_pics[636], width = 300)
        if selected_exercise == 'Standing High-To-Low Twist':
            st.image(demo_pics[638], width = 300)
        if selected_exercise == 'Standing Hip Abductions':
            st.image(demo_pics[640], width = 300)
        if selected_exercise == 'Standing Hip Adductions':
            st.image(demo_pics[643], width = 300)
        if selected_exercise == 'Standing Hip Extensions':
            st.image(demo_pics[646], width = 300)
        if selected_exercise == 'Standing Horizontal Press':
            st.image(demo_pics[650], width = 300)
        if selected_exercise == 'Standing Leg Curls':
            st.image(demo_pics[654], width = 300)
        if selected_exercise == 'Standing Overhead Press':
            st.image(demo_pics[657], width = 300)
        if selected_exercise == 'Step-Ups':
            st.image(demo_pics[661], width = 300)
        if selected_exercise == 'Stir-The-Pot':
            st.image(demo_pics[664], width = 300)
        if selected_exercise == 'Straight-Arm Lat Pulldown':
            st.image(demo_pics[666], width = 300)
        if selected_exercise == 'Supermans':
            st.image(demo_pics[668], width = 300)
        if selected_exercise == 'Thrusters':
            st.image(demo_pics[672], width = 300)
        if selected_exercise == 'Toes-To-Bar':
            st.image(demo_pics[675], width = 300)
        if selected_exercise == 'Treadmill':
            st.image(demo_pics[678], width = 300)
        if selected_exercise == 'Tricep Kickbacks':
            st.image(demo_pics[680], width = 300)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(demo_pics[684], width = 300)
        if selected_exercise == 'Turkish Get-Up':
            st.image(demo_pics[689], width = 300)
        if selected_exercise == 'Upright Rows':
            st.image(demo_pics[694], width = 300)
        if selected_exercise == "Waiter's Walk":
            st.image(demo_pics[700], width = 300)
        if selected_exercise == 'Walking Lunges':
            st.image(demo_pics[705], width = 300)
        if selected_exercise == 'Wall Balls':
            st.image(demo_pics[712], width = 300)
        if selected_exercise == 'Wall Sit':
            st.image(demo_pics[713], width = 300)
        if selected_exercise == 'Windshield Wipers':
            st.image(demo_pics[716], width = 300)
        if selected_exercise == 'Wrist Roller':
            st.image(demo_pics[720], width = 300)
        if selected_exercise == 'Zercher Squats':
            st.image(demo_pics[722], width = 300)
        if selected_exercise == 'Z-Press':
            st.image(demo_pics[724], width = 300)
        if selected_exercise == 'Front Loaded Carry':
            st.image(demo_pics[729], width = 300)
        if selected_exercise == 'Push Press':
            st.image(demo_pics[733], width = 300)

    with col_2:
        if selected_exercise == '3-Way Reaches':
            st.image(demo_pics[1], width = 300)
        if selected_exercise == 'Ab Bicycle':
            st.image(demo_pics[4], width = 300)
        if selected_exercise == 'Air Runner (Self-Powered Treadmill)':
            st.image(demo_pics[7], width = 300)
        if selected_exercise == 'Arnold Press':
            st.image(demo_pics[9], width = 300)
        if selected_exercise == 'Around-The-Worlds':
            st.image(demo_pics[11], width = 300)
        if selected_exercise == 'Assault Air Bike':
            st.image(demo_pics[15], width = 300)
        if selected_exercise == 'Back Extensions':
            st.image(demo_pics[17], width = 300)
        if selected_exercise == 'Back Squats':
            st.image(demo_pics[19], width = 300)
        if selected_exercise == 'Banana/Cannon Ball':
            st.image(demo_pics[21], width = 300)
        if selected_exercise == 'Banded Marches':
            st.image(demo_pics[25], width = 300)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[30], width = 300)
        if selected_exercise == 'Belt Squat':
            st.image(demo_pics[42], width = 300)
        if selected_exercise == 'Bench Press':
            st.image(demo_pics[45], width = 300)
        if selected_exercise == 'Bent Over Rows':
            st.image(demo_pics[48], width = 300)
        if selected_exercise == 'Bicep Curl':
            st.image(demo_pics[51], width = 300)
        if selected_exercise == 'Bird Dog':
            st.image(demo_pics[58], width = 300)
        if selected_exercise == 'Bottoms-Up Bench Press':
            st.image(demo_pics[60], width = 300)
        if selected_exercise == 'Bottoms-Up Incline Press':
            st.image(demo_pics[62], width = 300)
        if selected_exercise == 'Bottoms-Up Overhead Press':
            st.image(demo_pics[64], width = 300)
        if selected_exercise == 'Box Jumps':
            st.image(demo_pics[66], width = 300)
        if selected_exercise == 'Box Squats':
            st.image(demo_pics[70], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[73], width = 300)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(demo_pics[81], width = 300)
        if selected_exercise == 'Calf Raises':
            st.image(demo_pics[87], width = 300)
        if selected_exercise == 'Chest Flys':
            st.image(demo_pics[91], width = 300)
        if selected_exercise == 'Chin-Up Grip Lat Pulldown':
            st.image(demo_pics[97], width = 300)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(demo_pics[99], width = 300)
        if selected_exercise == 'Chin-Ups':
            st.image(demo_pics[105], width = 300)
        if selected_exercise == 'Clean & Press':
            st.image(demo_pics[107], width = 300)
        if selected_exercise == 'Clean High Pull':
            st.image(demo_pics[113], width = 300)
        if selected_exercise == 'Clean Pull':
            st.image(demo_pics[118], width = 300)
        if selected_exercise == 'Contact Twists':
            st.image(demo_pics[123], width = 300)
        if selected_exercise == 'Copenhagen Plank':
            st.image(demo_pics[125], width = 300)
        if selected_exercise == 'Dead Bugs':
            st.image(demo_pics[128], width = 300)
        if selected_exercise == 'Deadlift':
            st.image(demo_pics[131], width = 300)
        if selected_exercise == 'Decline Bench Press':
            st.image(demo_pics[137], width = 300)
        if selected_exercise == 'Decline Chest Flys':
            st.image(demo_pics[141], width = 300)
        if selected_exercise == 'Decline Reverse Crunch':
            st.image(demo_pics[147], width = 300)
        if selected_exercise == 'Decline Sit-Ups':
            st.image(demo_pics[149], width = 300)
        if selected_exercise == 'Depth Drops':
            st.image(demo_pics[151], width = 300)
        if selected_exercise == 'Depth Jumps':
            st.image(demo_pics[155], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[157], width = 300)
        if selected_exercise == 'Dips (Assisted)':
            st.image(demo_pics[164], width = 300)
        if selected_exercise == 'Dips':
            st.image(demo_pics[170], width = 300)
        if selected_exercise == 'Donkey Kicks':
            st.image(demo_pics[173], width = 300)
        if selected_exercise == 'Elliptical':
            st.image(demo_pics[177], width = 300)
        if selected_exercise == 'Face Pulls':
            st.image(demo_pics[180], width = 300)
        if selected_exercise == "Farmer's Walk":
            st.image(demo_pics[184], width = 300)
        if selected_exercise == 'Floor Press':
            st.image(demo_pics[187], width = 300)
        if selected_exercise == 'Flutter Kicks':
            st.image(demo_pics[193], width = 300)
        if selected_exercise == 'Foot Elevated Reverse Lunges':
            st.image(demo_pics[195], width = 300)
        if selected_exercise == 'Front Rack Lunges':
            st.image(demo_pics[199], width = 300)
        if selected_exercise == 'Front Raises':
            st.image(demo_pics[202], width = 300)
        if selected_exercise == 'Front Squats':
            st.image(demo_pics[206], width = 300)
        if selected_exercise == 'Glute Bridges':
            st.image(demo_pics[210], width = 300)
        if selected_exercise == 'Glute Ham Raises':
            st.image(demo_pics[216], width = 300)
        if selected_exercise == 'Goblet Squats':
            st.image(demo_pics[218], width = 300)
        if selected_exercise == 'Good Mornings':
            st.image(demo_pics[224], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[230], width = 300)
        if selected_exercise == 'Hack Squat':
            st.image(demo_pics[242], width = 300)
        if selected_exercise == 'Hammer Curls':
            st.image(demo_pics[245], width = 300)
        if selected_exercise == 'Hanging Knee Raises':
            st.image(demo_pics[250], width = 300)
        if selected_exercise == 'Hanging Leg Raises':
            st.image(demo_pics[252], width = 300)
        if selected_exercise == 'Hanging Oblique Knee Raises':
            st.image(demo_pics[254], width = 300)
        if selected_exercise == 'Hanging Windshield Wipers':
            st.image(demo_pics[257], width = 300)
        if selected_exercise == 'Heel Walks':
            st.image(demo_pics[260], width = 300)
        if selected_exercise == 'Hip Thrusters':
            st.image(demo_pics[262], width = 300)
        if selected_exercise == 'Hurdle Jumps':
            st.image(demo_pics[268], width = 300)
        if selected_exercise == 'In & Outs':
            st.image(demo_pics[274], width = 300)
        if selected_exercise == 'Incline Bench Press':
            st.image(demo_pics[276], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[280], width = 300)
        if selected_exercise == 'Inverted Row':
            st.image(demo_pics[287], width = 300)
        if selected_exercise == "I-Y-T's":
            st.image(demo_pics[290], width = 300)
        if selected_exercise == 'Jumping Rope':
            st.image(demo_pics[294], width = 300)
        if selected_exercise == 'Kettlebell Swings':
            st.image(demo_pics[296], width = 300)
        if selected_exercise == 'Knee Tuck Holds':
            st.image(demo_pics[298], width = 300)
        if selected_exercise == 'Knee Tuck Planks':
            st.image(demo_pics[300], width = 300)
        if selected_exercise == 'Kneeling Chest Pass':
            st.image(demo_pics[302], width = 300)
        if selected_exercise == 'Kneeling Crunches':
            st.image(demo_pics[304], width = 300)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(demo_pics[306], width = 300)
        if selected_exercise == 'Landmine Lateral Raises':
            st.image(demo_pics[313], width = 300)
        if selected_exercise == 'Landmine Rows':
            st.image(demo_pics[317], width = 300)
        if selected_exercise == 'Landmine Squats':
            st.image(demo_pics[319], width = 300)
        if selected_exercise == 'Lateral Ball Throws':
            st.image(demo_pics[324], width = 300)
        if selected_exercise == 'Lateral Band Walks':
            st.image(demo_pics[326], width = 300)
        if selected_exercise == 'Lateral Hurdle Jumps':
            st.image(demo_pics[328], width = 300)
        if selected_exercise == 'Lateral Lunges':
            st.image(demo_pics[331], width = 300)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(demo_pics[335], width = 300)
        if selected_exercise == 'Lateral Raises':
            st.image(demo_pics[341], width = 300)
        if selected_exercise == 'Lateral Sled Drag':
            st.image(demo_pics[344], width = 300)
        if selected_exercise == 'Leg Extensions':
            st.image(demo_pics[347], width = 300)
        if selected_exercise == 'Leg Press':
            st.image(demo_pics[351], width = 300)
        if selected_exercise == 'Lying Heel Touches':
            st.image(demo_pics[353], width = 300)
        if selected_exercise == 'Lying Leg Circles':
            st.image(demo_pics[355], width = 300)
        if selected_exercise == 'Lying Knee Tucks':
            st.image(demo_pics[357], width = 300)
        if selected_exercise == 'Lying Leg Curls (Floor)':
            st.image(demo_pics[360], width = 300)
        if selected_exercise == 'Lying Leg Curls (Machine)':
            st.image(demo_pics[363], width = 300)
        if selected_exercise == 'Lying Leg Raises':
            st.image(demo_pics[366], width = 300)
        if selected_exercise == 'Muscle Clean':
            st.image(demo_pics[368], width = 300)
        if selected_exercise == 'Neutral-Grip Lat Pulldown':
            st.image(demo_pics[373], width = 300)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(demo_pics[375], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[380], width = 300)
        if selected_exercise == 'Overhead Squat':
            st.image(demo_pics[388], width = 300)
        if selected_exercise == 'Overhead Tricep Extensions':
            st.image(demo_pics[390], width = 300)
        if selected_exercise == 'Overhead Walking Lunges':
            st.image(demo_pics[394], width = 300)
        if selected_exercise == 'Pallof Press':
            st.image(demo_pics[398], width = 300)
        if selected_exercise == 'Pallof Press Holds':
            st.image(demo_pics[401], width = 300)
        if selected_exercise == 'Pistol Squats':
            st.image(demo_pics[403], width = 300)
        if selected_exercise == 'Planks':
            st.image(demo_pics[409], width = 300)
        if selected_exercise == 'Plyo Lunges':
            st.image(demo_pics[412], width = 300)
        if selected_exercise == 'Preacher Curl':
            st.image(demo_pics[416], width = 300)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(demo_pics[421], width = 300)
        if selected_exercise == 'Pull Throughs':
            st.image(demo_pics[427], width = 300)
        if selected_exercise == 'Pull-Overs':
            st.image(demo_pics[429], width = 300)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(demo_pics[433], width = 300)
        if selected_exercise == 'Push-Ups':
            st.image(demo_pics[438], width = 300)
        if selected_exercise == 'Renegade Rows':
            st.image(demo_pics[444], width = 300)
        if selected_exercise == 'Reverse Flys':
            st.image(demo_pics[446], width = 300)
        if selected_exercise == 'Reverse Hypers':
            st.image(demo_pics[451], width = 300)
        if selected_exercise == 'Reverse Lunges':
            st.image(demo_pics[453], width = 300)
        if selected_exercise == 'Reverse Sled Drag':
            st.image(demo_pics[457], width = 300)
        if selected_exercise == 'Roll-Outs':
            st.image(demo_pics[459], width = 300)
        if selected_exercise == 'Romanian Deadlift':
            st.image(demo_pics[463], width = 300)
        if selected_exercise == 'Rope Climbs':
            st.image(demo_pics[469], width = 300)
        if selected_exercise == 'Rower':
            st.image(demo_pics[472], width = 300)
        if selected_exercise == 'Russian Twists':
            st.image(demo_pics[474], width = 300)
        if selected_exercise == 'Scissor Kicks':
            st.image(demo_pics[477], width = 300)
        if selected_exercise == 'Seal Rows':
            st.image(demo_pics[479], width = 300)
        if selected_exercise == 'Seated Calf Raises':
            st.image(demo_pics[484], width = 300)
        if selected_exercise == 'Seated Hip Abductions':
            st.image(demo_pics[489], width = 300)
        if selected_exercise == 'Seated Hip Adductions':
            st.image(demo_pics[492], width = 300)
        if selected_exercise == 'Seated Overhead Press':
            st.image(demo_pics[496], width = 300)
        if selected_exercise == 'Seated Rows':
            st.image(demo_pics[500], width = 300)
        if selected_exercise == 'Shin Curls':
            st.image(demo_pics[506], width = 300)
        if selected_exercise == 'Shin Hops':
            st.image(demo_pics[510], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[514], width = 300)
        if selected_exercise == 'Shoulder Internal Rotations':
            st.image(demo_pics[521], width = 300)
        if selected_exercise == 'Shoulder Taps':
            st.image(demo_pics[525], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[527], width = 300)
        if selected_exercise == 'Side Bends':
            st.image(demo_pics[535], width = 300)
        if selected_exercise == 'Side Lying Hip Abductions':
            st.image(demo_pics[540], width = 300)
        if selected_exercise == 'Side Plank Clamshells':
            st.image(demo_pics[544], width = 300)
        if selected_exercise == 'Side Plank Pulses':
            st.image(demo_pics[547], width = 300)
        if selected_exercise == 'Side Planks':
            st.image(demo_pics[550], width = 300)
        if selected_exercise == 'Side Step Planks':
            st.image(demo_pics[552], width = 300)
        if selected_exercise == "Single-Arm Farmer's Walk":
            st.image(demo_pics[554], width = 300)
        if selected_exercise == 'Single-Arm Landmine Press':
            st.image(demo_pics[556], width = 300)
        if selected_exercise == 'Single-Arm Lat Pulldown':
            st.image(demo_pics[560], width = 300)
        if selected_exercise == 'Single-Arm Overhead Press':
            st.image(demo_pics[564], width = 300)
        if selected_exercise == 'Single-Arm Rows':
            st.image(demo_pics[568], width = 300)
        if selected_exercise == 'Single-Arm Snatch':
            st.image(demo_pics[574], width = 300)
        if selected_exercise == 'Single-Leg Box Squats':
            st.image(demo_pics[576], width = 300)
        if selected_exercise == 'Single-Leg Calf Raises':
            st.image(demo_pics[580], width = 300)
        if selected_exercise == 'Single-Leg Glute Bridge':
            st.image(demo_pics[582], width = 300)
        if selected_exercise == 'Single-Leg Hip Thrusters':
            st.image(demo_pics[586], width = 300)
        if selected_exercise == 'Single-Leg Leg Press':
            st.image(demo_pics[589], width = 300)
        if selected_exercise == 'Single-Leg Romanian Deadlift':
            st.image(demo_pics[591], width = 300)
        if selected_exercise == 'Sissy Squats':
            st.image(demo_pics[595], width = 300)
        if selected_exercise == 'Sit-Ups':
            st.image(demo_pics[601], width = 300)
        if selected_exercise == 'Skull Crushers':
            st.image(demo_pics[604], width = 300)
        if selected_exercise == 'Sled Drag':
            st.image(demo_pics[609], width = 300)
        if selected_exercise == 'Sled Pulls':
            st.image(demo_pics[612], width = 300)
        if selected_exercise == 'Sled Push':
            st.image(demo_pics[614], width = 300)
        if selected_exercise == 'Sledgehammer Strikes':
            st.image(demo_pics[616], width = 300)
        if selected_exercise == 'Snatch':
            st.image(demo_pics[619], width = 300)
        if selected_exercise == 'Snatch High Pull':
            st.image(demo_pics[621], width = 300)
        if selected_exercise == 'Snatch Pull':
            st.image(demo_pics[626], width = 300)
        if selected_exercise == 'Speed Skater Jumps':
            st.image(demo_pics[630], width = 300)
        if selected_exercise == 'Squeeze Press':
            st.image(demo_pics[632], width = 300)
        if selected_exercise == 'Stairmaster':
            st.image(demo_pics[637], width = 300)
        if selected_exercise == 'Standing High-To-Low Twist':
            st.image(demo_pics[639], width = 300)
        if selected_exercise == 'Standing Hip Abductions':
            st.image(demo_pics[641], width = 300)
        if selected_exercise == 'Standing Hip Adductions':
            st.image(demo_pics[644], width = 300)
        if selected_exercise == 'Standing Hip Extensions':
            st.image(demo_pics[647], width = 300)
        if selected_exercise == 'Standing Horizontal Press':
            st.image(demo_pics[651], width = 300)
        if selected_exercise == 'Standing Leg Curls':
            st.image(demo_pics[655], width = 300)
        if selected_exercise == 'Standing Overhead Press':
            st.image(demo_pics[658], width = 300)
        if selected_exercise == 'Step-Ups':
            st.image(demo_pics[662], width = 300)
        if selected_exercise == 'Stir-The-Pot':
            st.image(demo_pics[665], width = 300)
        if selected_exercise == 'Straight-Arm Lat Pulldown':
            st.image(demo_pics[667], width = 300)
        if selected_exercise == 'Supermans':
            st.image(demo_pics[669], width = 300)
        if selected_exercise == 'Thrusters':
            st.image(demo_pics[673], width = 300)
        if selected_exercise == 'Toes-To-Bar':
            st.image(demo_pics[676], width = 300)
        if selected_exercise == 'Treadmill':
            st.image(demo_pics[679], width = 300)
        if selected_exercise == 'Tricep Kickbacks':
            st.image(demo_pics[681], width = 300)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(demo_pics[685], width = 300)
        if selected_exercise == 'Turkish Get-Up':
            st.image(demo_pics[690], width = 300)
        if selected_exercise == 'Upright Rows':
            st.image(demo_pics[695], width = 300)
        if selected_exercise == "Waiter's Walk":
            st.image(demo_pics[701], width = 300)
        if selected_exercise == 'Walking Lunges':
            st.image(demo_pics[706], width = 300)
        if selected_exercise == 'Wall Sit':
            st.image(demo_pics[714], width = 300)
        if selected_exercise == 'Windshield Wipers':
            st.image(demo_pics[717], width = 300)
        if selected_exercise == 'Wrist Roller':
            st.image(demo_pics[721], width = 300)
        if selected_exercise == 'Zercher Squats':
            st.image(demo_pics[723], width = 300)
        if selected_exercise == 'Z-Press':
            st.image(demo_pics[725], width = 300)
        if selected_exercise == 'Front Loaded Carry':
            st.image(demo_pics[730], width = 300)
        if selected_exercise == 'Push Press':
            st.image(demo_pics[734], width = 300)

    with col_3:
        if selected_exercise == '3-Way Reaches':
            st.image(demo_pics[2], width = 300)
        if selected_exercise == 'Around-The-Worlds':
            st.image(demo_pics[12], width = 300)
        if selected_exercise == 'Banana/Cannon Ball':
            st.image(demo_pics[22], width = 300)
        if selected_exercise == 'Banded Marches':
            st.image(demo_pics[26], width = 300)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[29], width = 300)
        if selected_exercise == 'Belt Squat':
            st.image(demo_pics[43], width = 300)
        if selected_exercise == 'Bench Press':
            st.image(demo_pics[46], width = 300)
        if selected_exercise == 'Bent Over Rows':
            st.image(demo_pics[49], width = 300)
        if selected_exercise == 'Bicep Curl':
            st.image(demo_pics[52], width = 300)
        if selected_exercise == 'Box Jumps':
            st.image(demo_pics[67], width = 300)
        if selected_exercise == 'Box Squats':
            st.image(demo_pics[71], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[74], width = 300)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(demo_pics[82], width = 300)
        if selected_exercise == 'Calf Raises':
            st.image(demo_pics[88], width = 300)
        if selected_exercise == 'Chest Flys':
            st.image(demo_pics[92], width = 300)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(demo_pics[100], width = 300)
        if selected_exercise == 'Clean & Press':
            st.image(demo_pics[108], width = 300)
        if selected_exercise == 'Clean High Pull':
            st.image(demo_pics[114], width = 300)
        if selected_exercise == 'Clean Pull':
            st.image(demo_pics[119], width = 300)
        if selected_exercise == 'Copenhagen Plank':
            st.image(demo_pics[126], width = 300)
        if selected_exercise == 'Dead Bugs':
            st.image(demo_pics[129], width = 300)
        if selected_exercise == 'Deadlift':
            st.image(demo_pics[132], width = 300)
        if selected_exercise == 'Decline Bench Press':
            st.image(demo_pics[138], width = 300)
        if selected_exercise == 'Decline Chest Flys':
            st.image(demo_pics[142], width = 300)
        if selected_exercise == 'Depth Drops':
            st.image(demo_pics[152], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[158], width = 300)
        if selected_exercise == 'Dips (Assisted)':
            st.image(demo_pics[165], width = 300)
        if selected_exercise == 'Dips':
            st.image(demo_pics[171], width = 300)
        if selected_exercise == 'Donkey Kicks':
            st.image(demo_pics[174], width = 300)
        if selected_exercise == 'Face Pulls':
            st.image(demo_pics[181], width = 300)
        if selected_exercise == "Farmer's Walk":
            st.image(demo_pics[185], width = 300)
        if selected_exercise == 'Floor Press':
            st.image(demo_pics[188], width = 300)
        if selected_exercise == 'Foot Elevated Reverse Lunges':
            st.image(demo_pics[196], width = 300)
        if selected_exercise == 'Front Rack Lunges':
            st.image(demo_pics[200], width = 300)
        if selected_exercise == 'Front Raises':
            st.image(demo_pics[203], width = 300)
        if selected_exercise == 'Front Squats':
            st.image(demo_pics[207], width = 300)
        if selected_exercise == 'Glute Bridges':
            st.image(demo_pics[211], width = 300)
        if selected_exercise == 'Goblet Squats':
            st.image(demo_pics[219], width = 300)
        if selected_exercise == 'Good Mornings':
            st.image(demo_pics[225], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[231], width = 300)
        if selected_exercise == 'Hack Squat':
            st.image(demo_pics[243], width = 300)
        if selected_exercise == 'Hammer Curls':
            st.image(demo_pics[246], width = 300)
        if selected_exercise == 'Hanging Oblique Knee Raises':
            st.image(demo_pics[255], width = 300)
        if selected_exercise == 'Hanging Windshield Wipers':
            st.image(demo_pics[258], width = 300)
        if selected_exercise == 'Hip Thrusters':
            st.image(demo_pics[263], width = 300)
        if selected_exercise == 'Hurdle Jumps':
            st.image(demo_pics[269], width = 300)
        if selected_exercise == 'Incline Bench Press':
            st.image(demo_pics[277], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[281], width = 300)
        if selected_exercise == 'Inverted Row':
            st.image(demo_pics[288], width = 300)
        if selected_exercise == "I-Y-T's":
            st.image(demo_pics[291], width = 300)
        if selected_exercise == 'Kneleing-To-Standing':
            st.image(demo_pics[307], width = 300)
        if selected_exercise == 'Landmine Lateral Raises':
            st.image(demo_pics[314], width = 300)
        if selected_exercise == 'Landmine Squats':
            st.image(demo_pics[320], width = 300)
        if selected_exercise == 'Lateral Hurdle Jumps':
            st.image(demo_pics[329], width = 300)
        if selected_exercise == 'Lateral Lunges':
            st.image(demo_pics[332], width = 300)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(demo_pics[336], width = 300)
        if selected_exercise == 'Lateral Raises':
            st.image(demo_pics[342], width = 300)
        if selected_exercise == 'Lateral Sled Drag':
            st.image(demo_pics[345], width = 300)
        if selected_exercise == 'Leg Extensions':
            st.image(demo_pics[348], width = 300)
        if selected_exercise == 'Lying Knee Tucks':
            st.image(demo_pics[358], width = 300)
        if selected_exercise == 'Lying Leg Curls (Floor)':
            st.image(demo_pics[361], width = 300)
        if selected_exercise == 'Lying Leg Curls (Machine)':
            st.image(demo_pics[364], width = 300)
        if selected_exercise == 'Muscle Clean':
            st.image(demo_pics[369], width = 300)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(demo_pics[376], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[381], width = 300)
        if selected_exercise == 'Overhead Tricep Extensions':
            st.image(demo_pics[391], width = 300)
        if selected_exercise == 'Overhead Walking Lunges':
            st.image(demo_pics[395], width = 300)
        if selected_exercise == 'Pallof Press':
            st.image(demo_pics[399], width = 300)
        if selected_exercise == 'Pistol Squats':
            st.image(demo_pics[404], width = 300)
        if selected_exercise == 'Planks':
            st.image(demo_pics[410], width = 300)
        if selected_exercise == 'Preacher Curl':
            st.image(demo_pics[417], width = 300)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(demo_pics[422], width = 300)
        if selected_exercise == 'Pull-Overs':
            st.image(demo_pics[430], width = 300)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(demo_pics[434], width = 300)
        if selected_exercise == 'Push-Ups':
            st.image(demo_pics[439], width = 300)
        if selected_exercise == 'Reverse Flys':
            st.image(demo_pics[447], width = 300)
        if selected_exercise == 'Reverse Lunges':
            st.image(demo_pics[454], width = 300)
        if selected_exercise == 'Roll-Outs':
            st.image(demo_pics[460], width = 300)
        if selected_exercise == 'Romanian Deadlift':
            st.image(demo_pics[464], width = 300)
        if selected_exercise == 'Rope Climbs':
            st.image(demo_pics[470], width = 300)
        if selected_exercise == 'Russian Twists':
            st.image(demo_pics[475], width = 300)
        if selected_exercise == 'Seal Rows':
            st.image(demo_pics[480], width = 300)
        if selected_exercise == 'Seated Calf Raises':
            st.image(demo_pics[485], width = 300)
        if selected_exercise == 'Seated Hip Abductions':
            st.image(demo_pics[490], width = 300)
        if selected_exercise == 'Seated Hip Adductions':
            st.image(demo_pics[493], width = 300)
        if selected_exercise == 'Seated Overhead Press':
            st.image(demo_pics[497], width = 300)
        if selected_exercise == 'Seated Rows':
            st.image(demo_pics[501], width = 300)
        if selected_exercise == 'Shin Curls':
            st.image(demo_pics[507], width = 300)
        if selected_exercise == 'Shin Hops':
            st.image(demo_pics[511], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[515], width = 300)
        if selected_exercise == 'Shoulder Internal Rotations':
            st.image(demo_pics[522], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[528], width = 300)
        if selected_exercise == 'Side Bends':
            st.image(demo_pics[536], width = 300)
        if selected_exercise == 'Side Lying Hip Abductions':
            st.image(demo_pics[541], width = 300)
        if selected_exercise == 'Side Plank Clamshells':
            st.image(demo_pics[545], width = 300)
        if selected_exercise == 'Side Plank Pulses':
            st.image(demo_pics[548], width = 300)
        if selected_exercise == 'Single-Arm Landmine Press':
            st.image(demo_pics[557], width = 300)
        if selected_exercise == 'Single-Arm Lat Pulldown':
            st.image(demo_pics[561], width = 300)
        if selected_exercise == 'Single-Arm Overhead Press':
            st.image(demo_pics[565], width = 300)
        if selected_exercise == 'Single-Arm Rows':
            st.image(demo_pics[569], width = 300)
        if selected_exercise == 'Single-Leg Box Squats':
            st.image(demo_pics[577], width = 300)
        if selected_exercise == 'Single-Leg Glute Bridge':
            st.image(demo_pics[583], width = 300)
        if selected_exercise == 'Single-Leg Hip Thrusters':
            st.image(demo_pics[587], width = 300)
        if selected_exercise == 'Single-Leg Romanian Deadlift':
            st.image(demo_pics[592], width = 300)
        if selected_exercise == 'Sissy Squats':
            st.image(demo_pics[596], width = 300)
        if selected_exercise == 'Skull Crushers':
            st.image(demo_pics[605], width = 300)
        if selected_exercise == 'Sled Drag':
            st.image(demo_pics[610], width = 300)
        if selected_exercise == 'Sledgehammer Strikes':
            st.image(demo_pics[617], width = 300)
        if selected_exercise == 'Snatch High Pull':
            st.image(demo_pics[622], width = 300)
        if selected_exercise == 'Snatch Pull':
            st.image(demo_pics[627], width = 300)
        if selected_exercise == 'Squeeze Press':
            st.image(demo_pics[633], width = 300)
        if selected_exercise == 'Standing Hip Abductions':
            st.image(demo_pics[642], width = 300)
        if selected_exercise == 'Standing Hip Adductions':
            st.image(demo_pics[645], width = 300)
        if selected_exercise == 'Standing Hip Extensions':
            st.image(demo_pics[648], width = 300)
        if selected_exercise == 'Standing Horizontal Press':
            st.image(demo_pics[652], width = 300)
        if selected_exercise == 'Standing Leg Curls':
            st.image(demo_pics[656], width = 300)
        if selected_exercise == 'Standing Overhead Press':
            st.image(demo_pics[659], width = 300)
        if selected_exercise == 'Step-Ups':
            st.image(demo_pics[663], width = 300)
        if selected_exercise == 'Supermans':
            st.image(demo_pics[670], width = 300)
        if selected_exercise == 'Thrusters':
            st.image(demo_pics[674], width = 300)
        if selected_exercise == 'Toes-To-Bar':
            st.image(demo_pics[677], width = 300)
        if selected_exercise == 'Tricep Kickbacks':
            st.image(demo_pics[682], width = 300)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(demo_pics[686], width = 300)
        if selected_exercise == 'Turkish Get-Up':
            st.image(demo_pics[691], width = 300)
        if selected_exercise == 'Upright Rows':
            st.image(demo_pics[696], width = 300)
        if selected_exercise == "Waiter's Walk":
            st.image(demo_pics[702], width = 300)
        if selected_exercise == 'Walking Lunges':
            st.image(demo_pics[707], width = 300)
        if selected_exercise == 'Wall Sit':
            st.image(demo_pics[715], width = 300)
        if selected_exercise == 'Windshield Wipers':
            st.image(demo_pics[718], width = 300)
        if selected_exercise == 'Z-Press':
            st.image(demo_pics[726], width = 300)
        if selected_exercise == 'Front Loaded Carry':
            st.image(demo_pics[731], width = 300)
        if selected_exercise == 'Push Press':
            st.image(demo_pics[735], width = 300)
        
    col_4, col_5, col_6 = st.columns(3)

    with col_4:
        if selected_exercise == 'Around-The-Worlds':
            st.image(demo_pics[13], width = 300)
        if selected_exercise == 'Banana/Cannon Ball':
            st.image(demo_pics[23], width = 300)
        if selected_exercise == 'Banded Marches':
            st.image(demo_pics[27], width = 300)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[32], width = 300)
        if selected_exercise == 'Bicep Curl':
            st.image(demo_pics[53], width = 300)
        if selected_exercise == 'Box Jumps':
            st.image(demo_pics[68], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[75], width = 300)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(demo_pics[83], width = 300)
        if selected_exercise == 'Calf Raises':
            st.image(demo_pics[89], width = 300)
        if selected_exercise == 'Chest Flys':
            st.image(demo_pics[93], width = 300)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(demo_pics[101], width = 300)
        if selected_exercise == 'Clean & Press':
            st.image(demo_pics[109], width = 300)
        if selected_exercise == 'Clean High Pull':
            st.image(demo_pics[115], width = 300)
        if selected_exercise == 'Clean Pull':
            st.image(demo_pics[120], width = 300)
        if selected_exercise == 'Deadlift':
            st.image(demo_pics[133], width = 300)
        if selected_exercise == 'Decline Bench Press':
            st.image(demo_pics[139], width = 300)
        if selected_exercise == 'Decline Chest Flys':
            st.image(demo_pics[143], width = 300)
        if selected_exercise == 'Depth Drops':
            st.image(demo_pics[153], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[159], width = 300)
        if selected_exercise == 'Dips (Assisted)':
            st.image(demo_pics[166], width = 300)
        if selected_exercise == 'Face Pulls':
            st.image(demo_pics[182], width = 300)
        if selected_exercise == 'Floor Press':
            st.image(demo_pics[189], width = 300)
        if selected_exercise == 'Foot Elevated Reverse Lunges':
            st.image(demo_pics[197], width = 300)
        if selected_exercise == 'Front Raises':
            st.image(demo_pics[204], width = 300)
        if selected_exercise == 'Glute Bridges':
            st.image(demo_pics[212], width = 300)
        if selected_exercise == 'Goblet Squats':
            st.image(demo_pics[220], width = 300)
        if selected_exercise == 'Good Mornings':
            st.image(demo_pics[226], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[232], width = 300)
        if selected_exercise == 'Hip Thrusters':
            st.image(demo_pics[264], width = 300)
        if selected_exercise == 'Hurdle Jumps':
            st.image(demo_pics[270], width = 300)
        if selected_exercise == 'Incline Bench Press':
            st.image(demo_pics[278], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[282], width = 300)
        if selected_exercise == "I-Y-T's":
            st.image(demo_pics[292], width = 300)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(demo_pics[308], width = 300)
        if selected_exercise == 'Landmine Lateral Raises':
            st.image(demo_pics[315], width = 300)
        if selected_exercise == 'Lateral Lunges':
            st.image(demo_pics[333], width = 300)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(demo_pics[337], width = 300)
        if selected_exercise == 'Leg Extensions':
            st.image(demo_pics[349], width = 300)
        if selected_exercise == 'Muscle Clean':
            st.image(demo_pics[370], width = 300)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(demo_pics[377], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[382], width = 300)
        if selected_exercise == 'Overhead Tricep Extensions':
            st.image(demo_pics[392], width = 300)
        if selected_exercise == 'Overhead Walking Lunges':
            st.image(demo_pics[396], width = 300)
        if selected_exercise == 'Pistol Squats':
            st.image(demo_pics[405], width = 300)
        if selected_exercise == 'Preacher Curl':
            st.image(demo_pics[418], width = 300)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(demo_pics[423], width = 300)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(demo_pics[435], width = 300)
        if selected_exercise == 'Push-Ups':
            st.image(demo_pics[440], width = 300)
        if selected_exercise == 'Reverse Flys':
            st.image(demo_pics[448], width = 300)
        if selected_exercise == 'Reverse Lunges':
            st.image(demo_pics[455], width = 300)
        if selected_exercise == 'Roll-Outs':
            st.image(demo_pics[461], width = 300)
        if selected_exercise == 'Romanian Deadlift':
            st.image(demo_pics[465], width = 300)
        if selected_exercise == 'Seal Rows':
            st.image(demo_pics[481], width = 300)
        if selected_exercise == 'Seated Calf Raises':
            st.image(demo_pics[486], width = 300)
        if selected_exercise == 'Seated Overhead Press':
            st.image(demo_pics[498], width = 300)
        if selected_exercise == 'Seated Rows':
            st.image(demo_pics[502], width = 300)
        if selected_exercise == 'Shin Curls':
            st.image(demo_pics[508], width = 300)
        if selected_exercise == 'Shin Hops':
            st.image(demo_pics[512], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[516], width = 300)
        if selected_exercise == 'Shoulder Internal Rotations':
            st.image(demo_pics[523], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[529], width = 300)
        if selected_exercise == 'Side Bends':
            st.image(demo_pics[537], width = 300)
        if selected_exercise == 'Side Lying Hip Abductions':
            st.image(demo_pics[542], width = 300)
        if selected_exercise == 'Single-Arm Landmine Press':
            st.image(demo_pics[558], width = 300)
        if selected_exercise == 'Single-Arm Lat Pulldown':
            st.image(demo_pics[562], width = 300)
        if selected_exercise == 'Single-Arm Overhead Press':
            st.image(demo_pics[566], width = 300)
        if selected_exercise == 'Single-Arm Rows':
            st.image(demo_pics[570], width = 300)
        if selected_exercise == 'Single-Leg Box Squats':
            st.image(demo_pics[578], width = 300)
        if selected_exercise == 'Single-Leg Glute Bridge':
            st.image(demo_pics[584], width = 300)
        if selected_exercise == 'Single-Leg Romanian Deadlift':
            st.image(demo_pics[590], width = 300)
        if selected_exercise == 'Sissy Squats':
            st.image(demo_pics[597], width = 300)
        if selected_exercise == 'Skull Crushers':
            st.image(demo_pics[606], width = 300)
        if selected_exercise == 'Snatch High Pull':
            st.image(demo_pics[623], width = 300)
        if selected_exercise == 'Snatch Pull':
            st.image(demo_pics[628], width = 300)
        if selected_exercise == 'Squeeze Press':
            st.image(demo_pics[634], width = 300)
        if selected_exercise == 'Standing Hip Extensions':
            st.image(demo_pics[649], width = 300)
        if selected_exercise == 'Standing Horizontal Press':
            st.image(demo_pics[653], width = 300)
        if selected_exercise == 'Standing Overhead Press':
            st.image(demo_pics[660], width = 300)
        if selected_exercise == 'Supermans':
            st.image(demo_pics[671], width = 300)
        if selected_exercise == 'Tricep Kickbacks':
            st.image(demo_pics[683], width = 300)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(demo_pics[687], width = 300)
        if selected_exercise == 'Turkish Get-Up':
            st.image(demo_pics[692], width = 300)
        if selected_exercise == 'Upright Rows':
            st.image(demo_pics[697], width = 300)
        if selected_exercise == "Waiter's Walk":
            st.image(demo_pics[703], width = 300)
        if selected_exercise == 'Walking Lunges':
            st.image(demo_pics[708], width = 300)
        if selected_exercise == 'Windshield Wipers':
            st.image(demo_pics[719], width = 300)
        if selected_exercise == 'Z-Press':
            st.image(demo_pics[727], width = 300)
        if selected_exercise == "Farmer's Walk":
            st.image(demo_pics[728], width = 300)
        if selected_exercise == 'Front Loaded Carry':
            st.image(demo_pics[732], width = 300)
        if selected_exercise == 'Push Press':
            st.image(demo_pics[736], width = 300)

    with col_5:
        if selected_exercise == 'Banded Marches':
            st.image(demo_pics[28], width = 300)
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[33], width = 300)
        if selected_exercise == 'Bicep Curl':
            st.image(demo_pics[54], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[76], width = 300)
        if selected_exercise == 'Bulgarian Split Squats':
            st.image(demo_pics[84], width = 300)
        if selected_exercise == 'Chest Flys':
            st.image(demo_pics[94], width = 300)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(demo_pics[102], width = 300)
        if selected_exercise == 'Clean & Press':
            st.image(demo_pics[110], width = 300)
        if selected_exercise == 'Clean High Pull':
            st.image(demo_pics[116], width = 300)
        if selected_exercise == 'Deadlift':
            st.image(demo_pics[134], width = 300)
        if selected_exercise == 'Decline Chest Flys':
            st.image(demo_pics[144], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[160], width = 300)
        if selected_exercise == 'Dips (Assisted)':
            st.image(demo_pics[167], width = 300)
        if selected_exercise == 'Floor Press':
            st.image(demo_pics[190], width = 300)
        if selected_exercise == 'Glute Bridges':
            st.image(demo_pics[213], width = 300)
        if selected_exercise == 'Goblet Squats':
            st.image(demo_pics[221], width = 300)
        if selected_exercise == 'Good Mornings':
            st.image(demo_pics[227], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[233], width = 300)
        if selected_exercise == 'Hip Thrusters':
            st.image(demo_pics[265], width = 300)
        if selected_exercise == 'Hurdle Jumps':
            st.image(demo_pics[271], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[283], width = 300)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(demo_pics[309], width = 300)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(demo_pics[338], width = 300)
        if selected_exercise == 'Nordic Ham Raises':
            st.image(demo_pics[378], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[383], width = 300)
        if selected_exercise == 'Pistol Squats':
            st.image(demo_pics[406], width = 300)
        if selected_exercise == 'Preacher Curl':
            st.image(demo_pics[419], width = 300)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(demo_pics[424], width = 300)
        if selected_exercise == 'Pull-Ups (Assisted)':
            st.image(demo_pics[436], width = 300)
        if selected_exercise == 'Push-Ups':
            st.image(demo_pics[441], width = 300)
        if selected_exercise == 'Reverse Flys':
            st.image(demo_pics[449], width = 300)
        if selected_exercise == 'Romanian Deadlift':
            st.image(demo_pics[466], width = 300)
        if selected_exercise == 'Seal Rows':
            st.image(demo_pics[482], width = 300)
        if selected_exercise == 'Seated Calf Raises':
            st.image(demo_pics[487], width = 300)
        if selected_exercise == 'Seated Rows':
            st.image(demo_pics[503], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[517], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[530], width = 300)
        if selected_exercise == 'Side Bends':
            st.image(demo_pics[538], width = 300)
        if selected_exercise == 'Single-Arm Rows':
            st.image(demo_pics[571], width = 300)
        if selected_exercise == 'Sissy Squats':
            st.image(demo_pics[598], width = 300)
        if selected_exercise == 'Skull Crushers':
            st.image(demo_pics[607], width = 300)
        if selected_exercise == 'Snatch High Pull':
            st.image(demo_pics[624], width = 300)
        if selected_exercise == 'Squeeze Press':
            st.image(demo_pics[635], width = 300)
        if selected_exercise == 'Tricep Pushdowns':
            st.image(demo_pics[688], width = 300)
        if selected_exercise == 'Turkish Get-Up':
            st.image(demo_pics[693], width = 300)
        if selected_exercise == 'Upright Rows':
            st.image(demo_pics[698], width = 300)
        if selected_exercise == "Waiter's Walk":
            st.image(demo_pics[704], width = 300)
        if selected_exercise == 'Walking Lunges':
            st.image(demo_pics[709], width = 300)
        if selected_exercise == 'Push Press':
            st.image(demo_pics[737], width = 300)

    with col_6:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[34], width = 300)
        if selected_exercise == 'Bicep Curl':
            st.image(demo_pics[55], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[77], width = 300)
        if selected_exercise == 'Chest Flys':
            st.image(demo_pics[95], width = 300)
        if selected_exercise == 'Chin-Ups (Assisted)':
            st.image(demo_pics[103], width = 300)
        if selected_exercise == 'Clean & Press':
            st.image(demo_pics[111], width = 300)
        if selected_exercise == 'Deadlift':
            st.image(demo_pics[135], width = 300)
        if selected_exercise == 'Decline Chest Flys':
            st.image(demo_pics[145], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[161], width = 300)
        if selected_exercise == 'Dips (Assisted)':
            st.image(demo_pics[168], width = 300)
        if selected_exercise == 'Floor Press':
            st.image(demo_pics[191], width = 300)
        if selected_exercise == 'Goblet Squats':
            st.image(demo_pics[222], width = 300)
        if selected_exercise == 'Good Mornings':
            st.image(demo_pics[228], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[234], width = 300)
        if selected_exercise == 'Hurdle Jumps':
            st.image(demo_pics[272], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[284], width = 300)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(demo_pics[310], width = 300)
        if selected_exercise == 'Lateral Plank Walks':
            st.image(demo_pics[339], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[384], width = 300)
        if selected_exercise == 'Pistol Squats':
            st.image(demo_pics[407], width = 300)
        if selected_exercise == 'Prone Lying Snow Angels':
            st.image(demo_pics[425], width = 300)
        if selected_exercise == 'Push-Ups':
            st.image(demo_pics[442], width = 300)
        if selected_exercise == 'Romanian Deadlift':
            st.image(demo_pics[467], width = 300)
        if selected_exercise == 'Seated Rows':
            st.image(demo_pics[504], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[518], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[531], width = 300)
        if selected_exercise == 'Single-Arm Rows':
            st.image(demo_pics[572], width = 300)
        if selected_exercise == 'Sissy Squats':
            st.image(demo_pics[599], width = 300)
        if selected_exercise == 'Upright Rows':
            st.image(demo_pics[699], width = 300)
        if selected_exercise == "Walking Lunges":
            st.image(demo_pics[710], width = 300)
        if selected_exercise == 'Push Press':
            st.image(demo_pics[738], width = 300)

    col_7, col_8, col_9 = st.columns(3)

    with col_7:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[35], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[78], width = 300)
        if selected_exercise == "Devil's Press":
            st.image(demo_pics[162], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[235], width = 300)
        if selected_exercise == 'Incline Chest Flys':
            st.image(demo_pics[285], width = 300)
        if selected_exercise == 'Kneeling-To-Standing':
            st.image(demo_pics[311], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[385], width = 300)
        if selected_exercise == 'Shoulder External Rotations':
            st.image(demo_pics[519], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[532], width = 300)
        if selected_exercise == 'Walking Lunges':
            st.image(demo_pics[711], width = 300)

    with col_8:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[36], width = 300)
        if selected_exercise == 'Broad Jumps':
            st.image(demo_pics[79], width = 300)
        if selected_exercise == "Ground-To-Shoulder":
            st.image(demo_pics[236], width = 300)
        if selected_exercise == 'Overhead Ball Throws':
            st.image(demo_pics[386], width = 300)
        if selected_exercise == 'Shrugs':
            st.image(demo_pics[533], width = 300)

    with col_9:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[37], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[237], width = 300)

    col_10, col_11, col_12 = st.columns(3)

    with col_10:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[38], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[238], width = 300)

    with col_11:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[39], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[239], width = 300)

    with col_12:
        if selected_exercise == 'Battle Rope Exercises':
            st.image(demo_pics[40], width = 300)
        if selected_exercise == 'Ground-To-Shoulder':
            st.image(demo_pics[240], width = 300)

if checkbox_2:
    st.header('My Physiotherapy Exercises:')
    df_2 = pd.DataFrame({'Exercise': ['', '', '', '', '', '', '', '', '', '', '', ''], 
                    'Weight': ['', '', '', '', '', '', '', '', '', '', '', ''], 
                    'Sets': ['', '', '', '', '', '', '', '', '', '', '', ''],
                    'Reps': ['', '', '', '', '', '', '', '', '', '', '', ''],
                    'Rest': ['', '', '', '', '', '', '', '', '', '', '', '']})
    
    num_exercises_col_1, num_exercises_col_2, num_exercises_col_3 = st.columns(3)

    with num_exercises_col_2:
        num_exercises = st.number_input('Number of Exercises in Your Physio Schedule (12 max):', 
                                        min_value = 1, max_value = 12, value = 1, step = 1)
    
    table_col_1, table_col_2, table_col_3, table_col_4, table_col_5 = st.columns(5)

    with table_col_1:
        if num_exercises == 1:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
        if num_exercises == 2:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
        if num_exercises == 3:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
        if num_exercises == 4:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
        if num_exercises == 5:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
        if num_exercises == 6:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
        if num_exercises == 7:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
            df_2['Exercise'][6] = st.text_input('Exercise #7:', key = 'Exercise #7')
        if num_exercises == 8:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
            df_2['Exercise'][6] = st.text_input('Exercise #7:', key = 'Exercise #7')
            df_2['Exercise'][7] = st.text_input('Exercise #8:', key = 'Exercise #8')
        if num_exercises == 9:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
            df_2['Exercise'][6] = st.text_input('Exercise #7:', key = 'Exercise #7')
            df_2['Exercise'][7] = st.text_input('Exercise #8:', key = 'Exercise #8')
            df_2['Exercise'][8] = st.text_input('Exercise #9:', key = 'Exercise #9')
        if num_exercises == 10:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
            df_2['Exercise'][6] = st.text_input('Exercise #7:', key = 'Exercise #7')
            df_2['Exercise'][7] = st.text_input('Exercise #8:', key = 'Exercise #8')
            df_2['Exercise'][8] = st.text_input('Exercise #9:', key = 'Exercise #9')
            df_2['Exercise'][9] = st.text_input('Exercise #10:', key = 'Exercise #10')
        if num_exercises == 11:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
            df_2['Exercise'][6] = st.text_input('Exercise #7:', key = 'Exercise #7')
            df_2['Exercise'][7] = st.text_input('Exercise #8:', key = 'Exercise #8')
            df_2['Exercise'][8] = st.text_input('Exercise #9:', key = 'Exercise #9')
            df_2['Exercise'][9] = st.text_input('Exercise #10:', key = 'Exercise #10')
            df_2['Exercise'][10] = st.text_input('Exercise #11:', key = 'Exercise #11')
        if num_exercises == 12:
            df_2['Exercise'][0] = st.text_input('Exercise #1:', key = 'Exercise #1')
            df_2['Exercise'][1] = st.text_input('Exercise #2:', key = 'Exercise #2')
            df_2['Exercise'][2] = st.text_input('Exercise #3:', key = 'Exercise #3')
            df_2['Exercise'][3] = st.text_input('Exercise #4:', key = 'Exercise #4')
            df_2['Exercise'][4] = st.text_input('Exercise #5:', key = 'Exercise #5')
            df_2['Exercise'][5] = st.text_input('Exercise #6:', key = 'Exercise #6')
            df_2['Exercise'][6] = st.text_input('Exercise #7:', key = 'Exercise #7')
            df_2['Exercise'][7] = st.text_input('Exercise #8:', key = 'Exercise #8')
            df_2['Exercise'][8] = st.text_input('Exercise #9:', key = 'Exercise #9')
            df_2['Exercise'][9] = st.text_input('Exercise #10:', key = 'Exercise #10')
            df_2['Exercise'][10] = st.text_input('Exercise #11:', key = 'Exercise #11')
            df_2['Exercise'][11] = st.text_input('Exercise #12:', key = 'Exercise #12')

    with table_col_2:
        if num_exercises == 1:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
        if num_exercises == 2:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
        if num_exercises == 3:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
        if num_exercises == 4:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
        if num_exercises == 5:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
        if num_exercises == 6:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
        if num_exercises == 7:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
            df_2['Weight'][6] = st.text_input('Weight (lbs./kg):', key = 'Weight #7')
        if num_exercises == 8:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
            df_2['Weight'][6] = st.text_input('Weight (lbs./kg):', key = 'Weight #7')
            df_2['Weight'][7] = st.text_input('Weight (lbs./kg):', key = 'Weight #8')
        if num_exercises == 9:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
            df_2['Weight'][6] = st.text_input('Weight (lbs./kg):', key = 'Weight #7')
            df_2['Weight'][7] = st.text_input('Weight (lbs./kg):', key = 'Weight #8')
            df_2['Weight'][8] = st.text_input('Weight (lbs./kg):', key = 'Weight #9')
        if num_exercises == 10:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
            df_2['Weight'][6] = st.text_input('Weight (lbs./kg):', key = 'Weight #7')
            df_2['Weight'][7] = st.text_input('Weight (lbs./kg):', key = 'Weight #8')
            df_2['Weight'][8] = st.text_input('Weight (lbs./kg):', key = 'Weight #9')
            df_2['Weight'][9] = st.text_input('Weight (lbs./kg):', key = 'Weight #10')
        if num_exercises == 11:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2')
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
            df_2['Weight'][6] = st.text_input('Weight (lbs./kg):', key = 'Weight #7')
            df_2['Weight'][7] = st.text_input('Weight (lbs./kg):', key = 'Weight #8')
            df_2['Weight'][8] = st.text_input('Weight (lbs./kg):', key = 'Weight #9')
            df_2['Weight'][9] = st.text_input('Weight (lbs./kg):', key = 'Weight #10')
            df_2['Weight'][10] = st.text_input('Weight (lbs./kg):', key = 'Weight #11')
        if num_exercises == 12:
            df_2['Weight'][0] = st.text_input('Weight (lbs./kg):', key = 'Weight #1')
            df_2['Weight'][1] = st.text_input('Weight (lbs./kg):', key = 'Weight #2') 
            df_2['Weight'][2] = st.text_input('Weight (lbs./kg):', key = 'Weight #3')
            df_2['Weight'][3] = st.text_input('Weight (lbs./kg):', key = 'Weight #4')
            df_2['Weight'][4] = st.text_input('Weight (lbs./kg):', key = 'Weight #5')
            df_2['Weight'][5] = st.text_input('Weight (lbs./kg):', key = 'Weight #6')
            df_2['Weight'][6] = st.text_input('Weight (lbs./kg):', key = 'Weight #7')
            df_2['Weight'][7] = st.text_input('Weight (lbs./kg):', key = 'Weight #8')
            df_2['Weight'][8] = st.text_input('Weight (lbs./kg):', key = 'Weight #9')
            df_2['Weight'][9] = st.text_input('Weight (lbs./kg):', key = 'Weight #10')
            df_2['Weight'][10] = st.text_input('Weight (lbs./kg):', key = 'Weight #11')
            df_2['Weight'][11] = st.text_input('Weight (lbs./kg):', key = 'Weight #12')

    with table_col_3:
        if num_exercises == 1:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
        if num_exercises == 2:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
        if num_exercises == 3:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
        if num_exercises == 4:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
        if num_exercises == 5:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
        if num_exercises == 6:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
        if num_exercises == 7:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
            df_2['Sets'][6] = st.text_input('Number of Sets:', key = 'Sets #7')
        if num_exercises == 8:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
            df_2['Sets'][6] = st.text_input('Number of Sets:', key = 'Sets #7')
            df_2['Sets'][7] = st.text_input('Number of Sets:', key = 'Sets #8')
        if num_exercises == 9:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
            df_2['Sets'][6] = st.text_input('Number of Sets:', key = 'Sets #7')
            df_2['Sets'][7] = st.text_input('Number of Sets:', key = 'Sets #8')
            df_2['Sets'][8] = st.text_input('Number of Sets:', key = 'Sets #9')
        if num_exercises == 10:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
            df_2['Sets'][6] = st.text_input('Number of Sets:', key = 'Sets #7')
            df_2['Sets'][7] = st.text_input('Number of Sets:', key = 'Sets #8')
            df_2['Sets'][8] = st.text_input('Number of Sets:', key = 'Sets #9')
            df_2['Sets'][9] = st.text_input('Number of Sets:', key = 'Sets #10')
        if num_exercises == 11:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2')
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
            df_2['Sets'][6] = st.text_input('Number of Sets:', key = 'Sets #7')
            df_2['Sets'][7] = st.text_input('Number of Sets:', key = 'Sets #8')
            df_2['Sets'][8] = st.text_input('Number of Sets:', key = 'Sets #9')
            df_2['Sets'][9] = st.text_input('Number of Sets:', key = 'Sets #10')
            df_2['Sets'][10] = st.text_input('Number of Sets:', key = 'Sets #11')
        if num_exercises == 12:
            df_2['Sets'][0] = st.text_input('Number of Sets:', key = 'Sets #1')
            df_2['Sets'][1] = st.text_input('Number of Sets:', key = 'Sets #2') 
            df_2['Sets'][2] = st.text_input('Number of Sets:', key = 'Sets #3')
            df_2['Sets'][3] = st.text_input('Number of Sets:', key = 'Sets #4')
            df_2['Sets'][4] = st.text_input('Number of Sets:', key = 'Sets #5')
            df_2['Sets'][5] = st.text_input('Number of Sets:', key = 'Sets #6')
            df_2['Sets'][6] = st.text_input('Number of Sets:', key = 'Sets #7')
            df_2['Sets'][7] = st.text_input('Number of Sets:', key = 'Sets #8')
            df_2['Sets'][8] = st.text_input('Number of Sets:', key = 'Sets #9')
            df_2['Sets'][9] = st.text_input('Number of Sets:', key = 'Sets #10')
            df_2['Sets'][10] = st.text_input('Number of Sets:', key = 'Sets #11')
            df_2['Sets'][11] = st.text_input('Number of Sets:', key = 'Sets #12')

    with table_col_4:
        if num_exercises == 1:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
        if num_exercises == 2:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
        if num_exercises == 3:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
        if num_exercises == 4:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
        if num_exercises == 5:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
        if num_exercises == 6:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
        if num_exercises == 7:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
            df_2['Reps'][6] = st.text_input('Number of Reps:', key = 'Reps #7')
        if num_exercises == 8:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
            df_2['Reps'][6] = st.text_input('Number of Reps:', key = 'Reps #7')
            df_2['Reps'][7] = st.text_input('Number of Reps:', key = 'Reps #8')
        if num_exercises == 9:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2')
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
            df_2['Reps'][6] = st.text_input('Number of Reps:', key = 'Reps #7')
            df_2['Reps'][7] = st.text_input('Number of Reps:', key = 'Reps #8')
            df_2['Reps'][8] = st.text_input('Number of Reps:', key = 'Reps #9')
        if num_exercises == 10:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2') 
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
            df_2['Reps'][6] = st.text_input('Number of Reps:', key = 'Reps #7')
            df_2['Reps'][7] = st.text_input('Number of Reps:', key = 'Reps #8')
            df_2['Reps'][8] = st.text_input('Number of Reps:', key = 'Reps #9')
            df_2['Reps'][9] = st.text_input('Number of Reps:', key = 'Reps #10')
        if num_exercises == 11:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2') 
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
            df_2['Reps'][6] = st.text_input('Number of Reps:', key = 'Reps #7')
            df_2['Reps'][7] = st.text_input('Number of Reps:', key = 'Reps #8')
            df_2['Reps'][8] = st.text_input('Number of Reps:', key = 'Reps #9')
            df_2['Reps'][9] = st.text_input('Number of Reps:', key = 'Reps #10')
            df_2['Reps'][10] = st.text_input('Number of Reps:', key = 'Reps #11')
        if num_exercises == 12:
            df_2['Reps'][0] = st.text_input('Number of Reps:', key = 'Reps #1')
            df_2['Reps'][1] = st.text_input('Number of Reps:', key = 'Reps #2') 
            df_2['Reps'][2] = st.text_input('Number of Reps:', key = 'Reps #3')
            df_2['Reps'][3] = st.text_input('Number of Reps:', key = 'Reps #4')
            df_2['Reps'][4] = st.text_input('Number of Reps:', key = 'Reps #5')
            df_2['Reps'][5] = st.text_input('Number of Reps:', key = 'Reps #6')
            df_2['Reps'][6] = st.text_input('Number of Reps:', key = 'Reps #7')
            df_2['Reps'][7] = st.text_input('Number of Reps:', key = 'Reps #8')
            df_2['Reps'][8] = st.text_input('Number of Reps:', key = 'Reps #9')
            df_2['Reps'][9] = st.text_input('Number of Reps:', key = 'Reps #10')
            df_2['Reps'][10] = st.text_input('Number of Reps:', key = 'Reps #11')
            df_2['Reps'][11] = st.text_input('Number of Reps:', key = 'Reps #12')

    with table_col_5:
        if num_exercises == 1:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
        if num_exercises == 2:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
        if num_exercises == 3:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
        if num_exercises == 4:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
        if num_exercises == 5:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
        if num_exercises == 6:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
        if num_exercises == 7:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
            df_2['Rest'][6] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #7')
        if num_exercises == 8:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2')
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
            df_2['Rest'][6] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #7')
            df_2['Rest'][7] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #8')
        if num_exercises == 9:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2') 
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
            df_2['Rest'][6] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #7')
            df_2['Rest'][7] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #8')
            df_2['Rest'][8] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #9')
        if num_exercises == 10:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2') 
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
            df_2['Rest'][6] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #7')
            df_2['Rest'][7] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #8')
            df_2['Rest'][8] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #9')
            df_2['Rest'][9] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #10')
        if num_exercises == 11:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2') 
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
            df_2['Rest'][6] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #7')
            df_2['Rest'][7] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #8')
            df_2['Rest'][8] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #9')
            df_2['Rest'][9] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #10')
            df_2['Rest'][10] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #11')
        if num_exercises == 12:
            df_2['Rest'][0] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #1')
            df_2['Rest'][1] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #2') 
            df_2['Rest'][2] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #3')
            df_2['Rest'][3] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #4')
            df_2['Rest'][4] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #5')
            df_2['Rest'][5] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #6')
            df_2['Rest'][6] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #7')
            df_2['Rest'][7] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #8')
            df_2['Rest'][8] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #9')
            df_2['Rest'][9] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #10')
            df_2['Rest'][10] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #11')
            df_2['Rest'][11] = st.text_input('Rest Between Sets (sec./min.):', key = 'Rest #12')


    user_workout = st.table(df_2)
    
    workout_to_csv = df_2.to_csv(index=False).encode('utf-8')

    st.download_button(
        'Download as CSV',
        physiotherapy_to_csv,
        'physiotherapy.csv',
        'text/csv',
        key='download-csv')


      

