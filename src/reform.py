# aoty format
def aotyFormat(s):
    text_lines = s.split('\n')
    formatted_text = ""

    for l in range(3, len(text_lines)):
        # titles only
        if l % 3 == 0:
            cur_line = text_lines[l]
            CUR_SCORE = int(text_lines[l+1])
            stars_amt = ""

            if CUR_SCORE >= 80 and CUR_SCORE <= 89:
                stars_amt = "{*}"
            elif CUR_SCORE >= 90 and CUR_SCORE <= 99:
                stars_amt = "{**}"
            elif CUR_SCORE == 100:
                stars_amt = "{***}"

            if cur_line[3] == ' ':
                print("[" + text_lines[l+1] + "]", cur_line[4:], stars_amt)
            else:
                print("[" + text_lines[l+1] + "]", cur_line[5:], stars_amt)