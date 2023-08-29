# calculates score
def calcScore(s):
    text_lines = s.split('\n')
    score_sum = 0.0
    track_amt = 0
    
    for l in range(3, len(text_lines)):
        # scores only
        if l % 3 == 0:
            try:
                CUR_SCORE = int(text_lines[l+1])
            except:
                print("INCORRECT FORMAT AT SCORE " + text_lines[l][0:4])
                break

            track_amt += 1
            bonus_x2 = (CUR_SCORE % 10) * 0.75
            
            if CUR_SCORE >= 80 and CUR_SCORE <= 89:
                score_sum += (CUR_SCORE + 10 + bonus_x2) * 0.92
            elif CUR_SCORE >= 90 and CUR_SCORE <= 99:
                score_sum += (CUR_SCORE + 15 + bonus_x2) * 0.95
            elif CUR_SCORE == 100:
                score_sum += CUR_SCORE + 25
            else:
                score_sum += CUR_SCORE

    print("Artist:", text_lines[0])
    print("Album:", text_lines[1],'\n')
    
    print("# of Tracks:", track_amt)
    print("Score Sum:", round(score_sum, 2))
    try: 
        print("Raw Score:", round((score_sum / track_amt), 2), "\n")
    except:
        print("Raw Score: TEXT NOT FORMATTED CORRECTLY")