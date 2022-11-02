def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    min_record = 0
    max_record = 0
    
    for score in scores[1:]:
        if min_score < score:
            min_record +=1
            min_score = score
        elif max_score > score:
            max_record +=1
            max_score = score
    return [min_record, max_record]