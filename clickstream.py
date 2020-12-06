# Create a class of nodes
class Node:
    def __init__(self, name, isEnd, connected=[0]):
        self.name = name  # name of the node (page).
        self.connected = connected  # a list of all connected nodes. (default = [0])
        self.isEnd = isEnd  # whether this node is the end of the graph (which only connects to prev node.)
        # but as soon as I created the property, I noticed that I dont need it anymore lol, so... just leave it there.

    def __repr__(self):
        return self.name

    def setConnected(self, connected):
        self.connected = connected

    def addConnected(self, node):
        self.connected.append(node)


# Setting Nodes.
ordering = Node("ordering", True, [0])
refund = Node("refund", True, [0])
order = Node("order", False, [refund, ordering])
ordering.setConnected([order])
refund.setConnected([order])

modify = Node("modify", True, [0])
recent = Node("recent", True, [0])
points = Node("points", True, [0])
personal = Node("personal", False, [modify, recent, points])
modify.setConnected([personal])
recent.setConnected([personal])
points.setConnected([personal])

userRank = Node("userRank", True, [0])
unrank = Node("unrank", True, [0])
prevRank = Node("prevRank", True, [0])
rank = Node("rank", False, [userRank, unrank, prevRank])
userRank.setConnected([rank])
unrank.setConnected([rank])
prevRank.setConnected([rank])

member = Node("member", False, [order, personal, rank])
order.addConnected(member)
personal.addConnected(member)
rank.addConnected(member)

faq = Node("faq", True, [0])
contact = Node("contact", True, [0])
online = Node("online", True, [0])
service = Node("service", False, [faq, contact, online])
faq.setConnected([service])
contact.setConnected([service])
online.setConnected([service])

fav = Node("fav", True, [0])
notify = Node("notify", True, [0])
pop = Node("pop", True, [0])

confirm = Node("confirm", False)
checkout = Node("checkout", False, [confirm])
cart = Node("cart", False, [checkout])
itemS1 = Node("itemS1", False, [cart])
searchRes = Node("searchRes", False, [itemS1])
checkout.addConnected(cart)
itemS1.addConnected(searchRes)

itemA1 = Node("itemA1", False, [cart])
itemB1 = Node("itemB1", False, [cart])
catA = Node("catA", False, [itemA1])
catB = Node("catB", False, [itemB1])
catList = Node("catList", False, [catA, catB])
catA.addConnected(catList)
catB.addConnected(catList)
itemA1.addConnected(catA)
itemB1.addConnected(catB)

home = Node("home", False, [notify, member, pop, catList, searchRes, cart, service, fav])
fav.setConnected([home])
notify.setConnected([home])
pop.setConnected([home])
cart.setConnected([checkout, itemS1, itemA1, itemB1, home])
member.addConnected(home)
catList.addConnected(home)
searchRes.addConnected(home)
service.addConnected(home)
confirm.setConnected([home])
# Finish setting nodes.


resultSet = []
resultSetTemp = []
clicks = 8  # The number of clicks can be modified.

# Generate the first click
for nodes in home.connected:
    result = [home, nodes]
    resultSet.append(result)
print("[#1]=============== Possible clickstreams in 1 click ===============")
print("Number of clickstreams in 1 click:" + str(len(resultSet)))
for result in resultSet:
    print('(' + ', '.join(map(str, result)) + ')')


# Generate the rest clicks
for x in range(clicks - 1):
    for res in resultSet:
        for nodes in res[x + 1].connected:
            resTemp = res.copy()
            resTemp.append(nodes)
            resultSetTemp.append(resTemp)
    resultSet = resultSetTemp.copy()
    print("[#" + str(x + 2) + "] =============== Possible clickstreams in " + str(x + 2) + " clicks ===============")
    print("Number of clickstreams in " + str(x + 2) + " clicks: " + str(len(resultSet)))
    for result in resultSet:
        print('(' + ', '.join(map(str, result)) + ')')
    resultSetTemp.clear()
