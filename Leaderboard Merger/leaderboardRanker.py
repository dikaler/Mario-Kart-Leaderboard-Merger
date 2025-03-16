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

scriptDirectory = os.path.dirname(os.path.abspath(__file__))

# Read CSV file from a folder
americanLeaderboard_csv = os.path.join(scriptDirectory, 'AmericaTop10Leaderboard.csv')
#columns = ['Player', 'Time']
americanRanking = pd.read_csv(americanLeaderboard_csv)
americanListHead = ListNode()
americanListDummy = americanListHead

europeanLeaderboard_csv = os.path.join(scriptDirectory, 'EuropeTop10Leaderboard.csv')
europeanRanking = pd.read_csv(europeanLeaderboard_csv)
europeanListHead = ListNode()
europeanListDummy = europeanListHead


createLinkedList(americanRanking, americanListDummy)
createLinkedList(europeanRanking, europeanListDummy)

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

mergedList = mergeTwoLists(americanListHead.next, europeanListHead.next)  # Pass the actual list nodes, not the dummy heads

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
merged_csv.to_csv(f"{scriptDirectory}/mergedLeaderboard.csv", index=False)

# Print the merged leaderboard and the count of nodes
print("\nMerged Leaderboard:")
print(mergedRanking)  # Print the merged leaderboard as a list of dictionaries