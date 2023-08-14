def discipline(dedication, persistence, commitment):
    dedication += 1  # dedication to discipline
    persistence += 1  # persistent in practicing discipline
    commitment += 1  # committed to personal growth

    if dedication and persistence and commitment:
        message = "Embrace discipline, persistence, and commitment. They work together to unlock your potential."
    else:
        message = "Stay dedicated, persistent, and committed. Discipline is your path to greatness."

    return message


dedication_present = True
persistence_present = True
commitment_present = True

motivational_message = discipline(dedication_present, persistence_present,
                                  commitment_present)
print(motivational_message)

# Embrace discipline, persistence, and commitment. They are the keys to unlocking your potential.
