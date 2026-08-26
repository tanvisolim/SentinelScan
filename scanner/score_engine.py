def calculate_score(results):

    if not results:
        return 0

    total = 0
    present = 0

    for key, value in results.items():

        if key == "Error":
            continue

        total += 1

        if value:
            present += 1

    if total == 0:
        return 0

    score = int((present / total) * 100)

    return score