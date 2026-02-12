"""
Finding key connections.
The datasets for this excersize is from "Data Science from Scratch" (pg. 3).

The objective of this excersize is to find the "key connections" from the set
of users and their interests.
"""

from collections import defaultdict
from collections import Counter

# Set of users
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
    { "id": 10, "name": "Jen" }
]

# Set of friendships among users(id)
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Set of users(id) and their interests
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

"""
To better represent the relationships among friends (and for greater
efficiency), we can convert the friendships into a map.

This allows us to look up the friends of a user in constant time.
"""
friendship_map = {}
for user in users:
    friendship_map[user["id"]] = []

for i, j in friendships:
    friendship_map[i].append(j) # Add i friends j
    friendship_map[j].append(i) # Add j friends i

print(friendship_map)

# 1. What is the average number of friends per user?
def friends_per_user(user):
    return len(friendship_map[user["id"]])

total_friends_user = sum(friends_per_user(user) for user in users)
avg_friends_per_user = total_friends_user / len(users)

print(f"Avg. Number of Friends per User: {avg_friends_per_user:.2f}\n")

# 2. Who are the most connected users?
num_friends_per_user = [(user["id"], friends_per_user(user)) for user in users]
num_friends_per_user.sort(
    key=lambda x: x[1],
    reverse=True
)

print(num_friends_per_user)

# 3. Who are the friends of friends (fof)?
def friends_of_friends_list(user):
    fofs = [
        fof_id
        for friend_id in friendship_map[user["id"]] # user friends
        for fof_id in friendship_map[friend_id]     # friends of user friends
        if fof_id != user["id"]                     # not user
    ]

    return set(fofs)

def friends_of_friends_count(user):
    user_id = user["id"]
    return Counter(
        fof_id
        for friend_id in friendship_map[user_id]  # user friends
        for fof_id in friendship_map[friend_id]   # friends of user friends
        if fof_id != user_id                      # Not user
        and fof_id not in friendship_map[user_id] # Not user friends
    )

# Print count of friends of friends
for user in users:
    print(f"User ID: {user['id']}")
    print(friends_of_friends_list(user))
    print(friends_of_friends_count(user))
    print()

# 4. What users have common interests?
# The first approach needs to examine a list for each query
def common_interests(target_interest):
    """Find IDs of all users who like target interest"""
    return [
        user_id
        for user_id, interest in interests
        if interest == target_interest
    ]

# Create a map key=interest, values=list of user IDs
# Now lookups are O(1)
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Create a map key=user ID, values=list of interests
# Lookups are O(1)
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

print(user_ids_by_interest["Python"])
print(user_ids_by_interest["Java"])

def most_common_interests(user):
    """Most interests in common with user"""
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

print(most_common_interests(users[0]))