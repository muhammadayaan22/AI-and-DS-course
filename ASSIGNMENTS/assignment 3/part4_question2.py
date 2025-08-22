scores = [40, 89, 90, 89, 23, 90, 50]
top_scores = list(set(scores))
top_scores.sort(reverse=True)

print("1st: ", top_scores[0])
print("2nd: ", top_scores[1])
