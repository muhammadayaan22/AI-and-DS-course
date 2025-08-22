def ts_score(score):
    if score > 60:
        return "pass"
    else:
        return "fail"

score = int(input("Enter your test score: "))
result = ts_score(score)
print(result)
