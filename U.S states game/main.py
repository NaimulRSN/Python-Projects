import turtle
import pandas
screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491,width=725)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()

guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                  prompt="What's another states name?")
    if answer_state=="Exit".lower():
        missing_states=[]
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

