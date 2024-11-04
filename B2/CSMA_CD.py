import matplotlib.pyplot as plt
import networkx as nx

def create_csma_cd_flowchart():
    G = nx.DiGraph()

    # Define each step in the CSMA/CD process with coordinates for layout
    steps = {
        "Start": (0, 3),
        "Check Channel Idle": (2, 3),
        "Channel Idle - Begin Transmission": (4, 4),
        "Channel Busy - Wait": (4, 2),
        "Transmit Frame": (6, 4),
        "Collision Detection": (6, 2),
        "Abort Transmission": (8, 2),
        "Back-Off and Retry": (10, 3),
        "Transmission Success": (8, 4)
    }

    # Add each step as a node in the graph
    for step, pos in steps.items():
        G.add_node(step, pos=pos)

    # Define transitions (edges) between the steps
    edges = [
        ("Start", "Check Channel Idle"),
        ("Check Channel Idle", "Channel Idle - Begin Transmission"),
        ("Check Channel Idle", "Channel Busy - Wait"),
        ("Channel Idle - Begin Transmission", "Transmit Frame"),
        ("Channel Busy - Wait", "Check Channel Idle"),
        ("Transmit Frame", "Transmission Success"),
        ("Transmit Frame", "Collision Detection"),
        ("Collision Detection", "Abort Transmission"),
        ("Abort Transmission", "Back-Off and Retry"),
        ("Back-Off and Retry", "Check Channel Idle")
    ]
    G.add_edges_from(edges)

    # Set the layout of the graph using predefined positions
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(12, 8))

    # Draw the network graph with customization for better visualization
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", 
            font_size=9, font_weight="bold", edge_color="gray", arrows=True, 
            arrowstyle="->", arrowsize=20)
    
    # Set a title for the flowchart
    plt.title("CSMA/CD (Carrier Sense Multiple Access with Collision Detection) Flowchart")
    plt.show()

create_csma_cd_flowchart()
