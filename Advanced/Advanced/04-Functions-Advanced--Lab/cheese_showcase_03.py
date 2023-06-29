def sorting_cheeses(**cheeses):
    sorted_cheeses = dict(sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0])))

    result = []
    for (cheese, values) in sorted_cheeses.items():
        result.append(cheese)
        values = sorted(values, reverse=True)
        result += values

    return "\n".join([str(x) for x in result])
