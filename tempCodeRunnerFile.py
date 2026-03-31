        if answer_state in all_states:
                
            state_data = data[data.state == answer_state]
                
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(state_data.state.item())

            guessed_states.append(answer_state)