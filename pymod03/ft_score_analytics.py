import sys
def main()->None:
    score = []
    print("=== Player Score Analytics ===")
    program_total = len(sys.argv)
    if program_total== 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for arg in sys.argv[1:]:
            try:
                num =int(arg)
                score.append(num)
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(score) == 0:
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ")
        else:
            print(f"Scores processed: {score}")
            print(f"Total players: {len(score)}")
            print(f"Total score: {sum(score)}")
            print(f"Average score: {sum(score)/len(score)}")
            print(f"High score: {max(score)}")
            print(f"Low score: {min(score)}")
            print(f"Score range: {max(score)-min(score)}")

if __name__ == "__main__":
    main()




    