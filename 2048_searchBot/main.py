# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic
import search_tree
import evaluation
from evaluation import total_score


# Driver code

def main(weights):
    mat = logic.start_game()

    while True:

        # taking the user input
        # for next step
        x = search_tree.find_best_move(mat, weights)

        # we have to move up
        if x == 'U':

            # call the move_up function
            mat = logic.move_up(mat)

            # get the current state and print it
            status = logic.get_current_state(mat)


            # if game not over then continue
            # and add a new two
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)

            # else break the loop
            else:
                break

        # the above process will be followed
        # in case of each type of move
        # below

        # to move down
        elif (x == 'D'):
            mat = logic.move_down(mat)
            status = logic.get_current_state(mat)

            if (status == 'GAME NOT OVER'):
                logic.add_new_2(mat)
            else:
                break

        # to move left
        elif (x == 'L'):
            mat = logic.move_left(mat)
            status = logic.get_current_state(mat)
            print(status)
            if (status == 'GAME NOT OVER'):
                logic.add_new_2(mat)

            else:
                break

        # to move right
        elif (x == 'R'):
            mat = logic.move_right(mat)
            status = logic.get_current_state(mat)
            print(status)
            if (status == 'GAME NOT OVER'):
                logic.add_new_2(mat)

            else:
                break
        else:
            print("--GAME OVER--")
            break

    print(mat[0])
    print(mat[1])
    print(mat[2])
    print(mat[3])
    return logic.game_score(mat)
