import pandas as pd
import os

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(ranking, linkedlist):
    for index, row in ranking.iterrows():
        linkedlist.next = ListNode([row['Player'], row['Time']])
        linkedlist = linkedlist.next

# Function to get file paths from user input
def get_file_path(region):
    filePath = input(f"Enter the file path for the {region} leaderboard CSV file: ").strip()
    pathExists = False
    
    while pathExists == False:
        if os.path.exists(filePath):
            pathExists = True
            return filePath
        else:
            filePath = input(f"Please try again: ").strip()

scriptDirectory = os.path.dirname(os.path.abspath(__file__))

# Get file paths
leaderboard1Name = input("Enter the name of the first region's leaderboard: ")
leaderboard1 = get_file_path(leaderboard1Name)
leaderboard2Name = input("Enter the name of the second region's leaderboard: ")
leaderboard2 = get_file_path(leaderboard2Name)

#columns = ['Player', 'Time']
leaderboard1Ranking = pd.read_csv(leaderboard1)
leaderboard1ListHead = ListNode()
leaderboard1ListDummy = leaderboard1ListHead

leaderboard2Ranking = pd.read_csv(leaderboard2)
leaderboard2ListHead = ListNode()
leaderboard2ListDummy = leaderboard2ListHead

createLinkedList(leaderboard1Ranking, leaderboard1ListDummy)
createLinkedList(leaderboard2Ranking, leaderboard2ListDummy)

def printLinkedList(head):
    current = head.next  # Skip the dummy head
    result = []
    while current:
        result.append(current.val)  # Add 'Player' and 'Time' values to the result list
        current = current.next
    return result

def mergeTwoLists(list1, list2):
    head = ListNode()
    dummy = head

    while list1 and list2:
        if list1.val[1] < list2.val[1]:
            dummy.next = list1
            list1 = list1.next
        else:
            dummy.next = list2
            list2 = list2.next
        dummy = dummy.next
    
    dummy.next = list1 or list2
    
    while dummy.next:
        dummy = dummy.next

    return head.next

mergedList = mergeTwoLists(leaderboard1ListHead.next, leaderboard2ListHead.next)  # Pass the actual list nodes, not the dummy heads

def linkedListToList(head):
    current = head
    position = 1
    result = []
    while current:
        result.append({'Rank': position,'Player': current.val[0], 'Time': current.val[1]})
        current = current.next
        position += 1
    return result

# Convert the merged list to a pandas DataFrame
mergedRanking = linkedListToList(mergedList)
merged_csv = pd.DataFrame(mergedRanking)

# Save the DataFrame to a CSV file
output_path = f"{scriptDirectory}/mergedleaderboard.csv"
merged_csv.to_csv(output_path, index=False)

# Print the merged leaderboard and the count of nodes
print("\nMerged leaderboard:")
print(mergedRanking)  # Print the merged leaderboard as a list of dictionaries
print(f"Merged leaderboard saved at: {output_path}")