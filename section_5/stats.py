import random

def randomly_sample_and_filter_participants(
    participants: list, 
    sample_size: int, 
    min_age: int, 
    max_age: int, 
    min_height: int, 
    max_height: int
):
    """Participants is a list of tuples, containing the age and height of each participant
    participants = [
                      {age: 25, height: 180}, 
                      {age: 30, height: 170}, 
                      {age: 35, height: 160}, 
    ]
    """
    sampled_participants = get_sample_of_participants(participants, sample_size)
    age_filtered = within_age_range(sampled_participants, min_age, max_age)
    age_and_height_filtered = [age_filtered]
    return age_and_height_filtered

def get_sample_of_participants(participants, sample_size):
    # Get the indexes to sample
    indexes = random.sample(range(len(participants)), sample_size)

    # Get the sampled participants
    sampled_participants = []
    for i in indexes:
        sampled_participants.append(participants[i])

def within_age_range(participants, min_age, max_age):
    # Remove participants that are outside the age range
    age_filtered = []
    for participant in participants:
        if participant['age'] >= min_age and participant['age'] <= max_age:
            age_filtered.append(participant)
    return age_filtered
    
def within_height_range(participants, min_height, max_height):
    # Remove participants that are outside the height range
    height_filtered = []
    for participant in participants:
        if participant['height'] >= min_height and participant['height'] <= max_height:
            height_filtered.append(participant)
    return height_filtered

